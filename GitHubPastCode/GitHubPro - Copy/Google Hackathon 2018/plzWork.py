from gtts import gTTS
import pyglet
import time , os
import win32com.client as wincl
import pyttsx3
from gtts import gTTS
import pyglet
import time , os
import win32com.client as wincl
import pyttsx3
import tkinter
import tkinter.messagebox
import random



class MyGUI:

    def __init__(self):

        
        Font='times 18 bold '
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        
        
        

        self.prompt_label = tkinter.Label(self.top_frame, \
                     text='Storytime with Py:',font= Font)

        self.my_button = tkinter.Button(self.mid_frame, \
                                   text = 'Good night Moon', font = Font, 
                                   bg ='Blue',\
                                   command=self.do_everything)
        self.my_button1 = tkinter.Button(self.mid_frame, \
                                   text = 'Time', font = Font, 
                                   bg ='Red',\
                                   command=self.do_everything1)
        self.my_button2 = tkinter.Button(self.mid_frame, \
                                   text = 'Green Eggs and Ham', font = Font, 
                                   bg ='Green',\
                                   command=self.do_everything2)
        self.my_button3 = tkinter.Button(self.mid_frame, \
                                   text = 'Oh, The Places you^ll Go', font = Font, 
                                   bg ='Pink',\
                                   command=self.do_everything3)
        self.check_entry = tkinter.Entry(self.mid_frame, \
                                        width=50)
 

        self.quit_button = tkinter.Button(self.bottom_frame, \
                                   text = 'Quit',\
                                   command=self.main_window.destroy)

        self.check_entry.pack(side='top')
        
        self.prompt_label.pack(side='top')
        self.my_button.pack(side='left')
        self.my_button1.pack(side='left')
        self.my_button2.pack(side='right')
        self.my_button3.pack(side='right')
        self.quit_button.pack(side='bottom')
        self.top_frame.pack()
        self.mid_frame.pack(side='top')
        self.bottom_frame.pack(side='bottom')
        tkinter.mainloop()

    def do_everything(self):
        engine =pyttsx3.init()
        sound= engine.getProperty('voices')

        engine.setProperty('voice',sound[4].id,)
        engine.setProperty('voice',sound[4].id)
        nvr=200
        engine.setProperty('rate', nvr)
        text=""

        with open("try.txt","r")as file:
            for line in file:
                text=text + line
        tts = gTTS(text,'en',)


        engine.say(text)
        engine.runAndWait()

    def do_everything1(self):
        engine =pyttsx3.init()
        sound= engine.getProperty('voices')

        engine.setProperty('voice',sound[4].id,)
        engine.setProperty('voice',sound[4].id)
        nvr=200
        engine.setProperty('rate', nvr)
        text=""

        with open("try1.txt","r")as file:
            for line in file:
                text=text + line
        tts = gTTS(text,'en',)

        engine.say(text)
        engine.runAndWait()
        
    def do_everything2(self):
        engine =pyttsx3.init()
        sound= engine.getProperty('voices')

        engine.setProperty('voice',sound[4].id,)
        engine.setProperty('voice',sound[4].id)
        nvr=200
        engine.setProperty('rate', nvr)
        text=""

        with open("try2.txt","r")as file:
            for line in file:
                text=text + line
        tts = gTTS(text,'en',)


        engine.say(text)
        engine.runAndWait()

    def do_everything3(self):
        engine =pyttsx3.init()
        sound= engine.getProperty('voices')

        engine.setProperty('voice',sound[4].id,)
        engine.setProperty('voice',sound[4].id)
        nvr=200
        engine.setProperty('rate', nvr)
        text=""

        with open("try3.txt","r")as file:
            for line in file:
                text=text + line
        tts = gTTS(text,'en',)

        engine.say(text)
        engine.runAndWait()
        
    
        
    
        
   
       
my_gui = MyGUI()
