import pyalgotrade.strategy as strategy
import pyalgotrade.technical.ma as ma
import pyalgotrade.plotter as plotter
import pyalgotrade.barfeed.csvfeed as csvfeed
import pyalgotrade.bar as bar
import pyalgotrade.stratanalyzer.returns as ret
import pyalgotrade.stratanalyzer.sharpe as sharpe
import pyalgotrade.stratanalyzer.drawdown as drawdown
import pyalgotrade.stratanalyzer.trades as trades
from pyalgotrade.broker import backtesting

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

#MA model
class MovingAverageStrategy(strategy.BacktestingStrategy):

	def __init__(self,feed,instrument,nfast,nslow):
		# define the initial budget
		super(MovingAverageStrategy,self).__init__(feed,INITIAL_BUDGET)
		#track the position
		self.position = None
		
		self.instrument = instrument
		
		self.setUseAdjustedValues(True)
		
		self.fastMA = ma.EMA(feed[instrument].getPriceDataSeries(),nfast)
		
		self.slowMA = ma.EMA(feed[instrument].getPriceDataSeries(),nslow)
		
	def getFastMA(self):
		return self.fastMA
		
	def getSlowMA(self):
		return self.slowMA
		
	#this is where the MA crossover strategy is implemented
	#this method is called when new bars are available
	#when fast > slow MA -> open a long position 
	#when fast < slow MA -> close the long position
	def onBars(self,bars):
		
		#MA with preiod p needs p previous values
		if self.slowMA[-1] is None:
			return
		
		#if we have not opened a long position so far then we open one
		if self.position is None:
			if self.fastMA[-1] > self.slowMA[-1]:
				self.position = self.enterLong(self.instrument,NSHARES,True)
		elif self.fastMA[-1] < self.slowMA[-1]:
			self.position.exitMarket()
			self.position = None
	
	
	def onEnterOk(self,position):
		trade_info = position.getEntryOrder().getExecutionInfo()
		self.info("Buy stock at $%.2f and actual equity: $%.2f"%(trade_info.getPrice(),self.getBroker().getEquity()))
		
		
	def onExitOk(self,position):
		trade_info = position.getExitOrder().getExecutionInfo()
		self.info("Sell stock at $%.2f"%(trade_info.getPrice()))
	
if __name__ == "__main__":

	cost_per_trade = 4.95
	instrument = 'TSLA'
	fpath='C:/Users/caive/Documents/'
	ftype='.csv'
	fname=fpath+instrument+ftype

	# slowperiod and fastperiod values 
	fastminval = 3
	fastmaxval = 50
	fastvec = list(range(fastminval, fastmaxval+1))
	slowmult = [1.5,2,2.5,3,3.5,4]
	slowlist = []
	fastlist = []
	for fastPeriod in fastvec:
		tmp_slow = []
		tmp_fast = []
		for multval in slowmult:
			tmp_slow.append(int(multval*fastPeriod))			
			tmp_fast.append(fastPeriod)
		slowlist.append(tmp_slow)		
		fastlist.append(tmp_fast)

	#backtest fastperiod/slowperiod pair 
	net_profit_list = []
	for i in range(len(fastvec)):
		fastPeriod = fastvec[i]
		tmp_profit_list = []
		for slowPeriod in slowlist[i]:

			print([fastPeriod,slowPeriod])

			
			INITIAL_BUDGET = 15000
			NSHARES = 20

			#the data is in the CSV file 
			feed = csvfeed.GenericBarFeed(bar.Frequency.DAY)
			feed.addBarsFromCSV(instrument,fname)

			# define the time for the moving average models 
			movingAverageStrategy = MovingAverageStrategy(feed,instrument,fastPeriod,slowPeriod)
	
			#define the cost of trading 
			movingAverageStrategy.getBroker().setCommission(backtesting.FixedPerTrade(cost_per_trade))

			#analyze the returns during the backtest
			returnAnalyzer = ret.Returns()
			movingAverageStrategy.attachAnalyzer(returnAnalyzer)
	
			#analyze the Sharpe ratio during backtest
			sharpeRatioAnalyzer = sharpe.SharpeRatio()
			movingAverageStrategy.attachAnalyzer(sharpeRatioAnalyzer)
	
			# analyze the trades 
			tradesAnalyzer = trades.Trades()
			movingAverageStrategy.attachAnalyzer(tradesAnalyzer)
	
			
			movingAverageStrategy.run()
	
			print('Initial equity: $',INITIAL_BUDGET)
			print('Portfolio net trading profit and loss: $%.2f' % tradesAnalyzer.getAll().sum())
			tmp_profit_list.append(tradesAnalyzer.getAll().sum())

			del movingAverageStrategy

		net_profit_list.append(tmp_profit_list)

	
	fast_length=len(fastvec)
	slow_length=len(slowmult)
	X = np.zeros((fast_length,slow_length))
	Y = np.zeros((fast_length,slow_length))	
	Z = np.zeros((fast_length,slow_length))
	for i in range(fast_length):
		for j in range(slow_length):
			X[i,j] = fastlist[i][j]
			Y[i,j] = slowlist[i][j]
			Z[i,j] = net_profit_list[i][j]
	
	print()
	maxptr = np.unravel_index(np.argmax(Z, axis=None), Z.shape)
	print('Fast MA with max profit = ', int(X[maxptr]))
	print('Slow MA with max profit = ', int(Y[maxptr]))
	print('Max profit = ', Z[maxptr])

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
	fig.colorbar(surf, shrink=0.5, aspect=5)
	plt.title(instrument)
	ax.set_xlabel('Fast')
	ax.set_ylabel('Slow')
	ax.set_zlabel('Profit $')
	plt.show()


