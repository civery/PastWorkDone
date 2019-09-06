from gtts import gTTS
import pyglet
import time , os
import win32com.client as wincl
import pyttsx3

engine =pyttsx3.init()
sound= engine.getProperty('voices')
a=int(input())
engine.setProperty('voice',sound[a].id,)
engine.setProperty('voice',sound[a].id)
nvr=175
engine.setProperty('rate', nvr)

text=""

with open("try.txt","r")as file:
    for line in file:
        text=text + line
tts = gTTS(text,'en',)


engine.say(text)
engine.runAndWait()


text1=""
with open("try1.txt","r")as file:
    for line in file:
        text1=text1 + line
tts = gTTS(text1,'en',)


engine.say(text1)
engine.runAndWait()







