import pyalgotrade.strategy as strategy
import pyalgotrade.technical.ma as ma
from pyalgotrade.technical import rsi
import pyalgotrade.plotter as plotter
import pyalgotrade.barfeed.csvfeed as csvfeed
import pyalgotrade.bar as bar
import pyalgotrade.stratanalyzer.returns as ret
import pyalgotrade.stratanalyzer.sharpe as sharpe
import pyalgotrade.stratanalyzer.drawdown as drawdown
import pyalgotrade.stratanalyzer.trades as trades
import itertools
from pyalgotrade.optimizer import local

# initial budget
INITIAL_BUDGET = 15000
NSHARES = 10

#MA model
class RSIMovingAverageStrategy(strategy.BacktestingStrategy):

	def __init__(self,feed,instrument,fastPeriod,slowPeriod,rsiPeriod,overboughtThreshold,oversoldThreshold):
		# define the initial budget
		super(RSIMovingAverageStrategy,self).__init__(feed,INITIAL_BUDGET)
		# track the position
		
		self.longPosition = None
		self.shortPosition = None
		self.oversoldThreshold = oversoldThreshold
		self.overboughtThreshold = overboughtThreshold
		
		self.instrument = instrument
		# adjusted closing prices instead of regular closing prices
		self.setUseAdjustedValues(True)
		#fast MA indicator 
		self.fastMA = ma.SMA(feed[instrument].getPriceDataSeries(),fastPeriod)
		#slow MA indicator 
		self.slowMA = ma.SMA(feed[instrument].getPriceDataSeries(),slowPeriod)
		# RSI model
		self.rsi = rsi.RSI(feed[instrument].getPriceDataSeries(),rsiPeriod)
		
	def getFastMA(self):
		return self.fastMA
		
	def getSlowMA(self):
		return self.slowMA
		
	def getRSI(self):
		return self.rsi
		
	# MA crossover strategy is implemented
	# new bars  available
	def onBars(self,bars):
		
		if self.fastMA[-1] is None or self.slowMA[-1] is None or self.rsi[-1] is None:
			return
		
		
		if self.longPosition is not None:
				if self.exitLongSignal():
					self.longPosition.exitMarket()
					self.longPosition = None
		
		elif self.shortPosition is not None:
				if self.exitShortSignal():
					self.shortPosition.exitMarket()
					self.shortPosition = None
		
		else:
		
			
			if self.enterLongSignal():
				self.longPosition = self.enterLong(self.instrument,NSHARES,True)
			
			elif self.enterShortSignal():
				self.shortPosition = self.enterShort(self.instrument,NSHARES,True)
		
	def enterLongSignal(self):
		return self.fastMA[-1]>self.slowMA[-1] and self.rsi[-1]<self.oversoldThreshold
		
	def enterShortSignal(self):
		return self.fastMA[-1]<self.slowMA[-1] and self.rsi[-1]>self.overboughtThreshold

	def exitLongSignal(self):
		return self.fastMA[-1]<self.slowMA[-1]
		
	def exitShortSignal(self):
		return self.fastMA[-1]>self.slowMA[-1]
	
if __name__ == "__main__":


	
	instrument = ['AAPL']

	fpath='C:/Users/caive/Documents/'
	ftype='.csv'
	fname=fpath+instrument[0]+ftype

	
	slowPeriod = (50,60,80,100,150,170,200)   
	fastPeriod = (5,10,20,30,40)
	rsiPeriod = (2,3,5,7,10,14)
	oversoldThreshold = (10,20,30)
	overboughtThreshold = (70,80,90)

#*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/#

	# generate all the permutations
	all = itertools.product(instrument,fastPeriod,slowPeriod,rsiPeriod,
		overboughtThreshold,oversoldThreshold)
	
	#data is in the CSV file 
	feed = csvfeed.GenericBarFeed(bar.Frequency.DAY)
	feed.addBarsFromCSV(instrument[0],fname)
	
	# run the optimization parallel 
	local.run(RSIMovingAverageStrategy,feed,all)

