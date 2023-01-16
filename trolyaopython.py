import pyttsx3
import datetime
import sys
from random import randint
import json
import re
from random import randint, choice
import requests
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import perf_counter, strftime
from gtts import gTTS, tts
import speech_recognition as sr
from gtts import gTTS 
import webbrowser as wb
import os
import cv2
import pyautogui
import wikipedia
import playsound
import psutil


nhat=pyttsx3.init()
voice=nhat.getProperty('voices')
nhat.setProperty('voice',voice[1].id) #void[0].id là nam ngược lại là nữ

def speak(audio):
    print('Nhat: ' + audio)
    nhat.say(audio)
    nhat.runAndWait()
speak("Hello , i am the botchat created by Minh Nhat and i will answer all question you can ")

def time():
    Time=datetime.datetime.now().strftime("Now is a %I: %M : %p") #I hours , M minutes , p sessions
    speak(Time)

def welcome():
    hour=datetime.datetime.now().hour
    if hour >=1 and hour <5 :
        speak("Hi, It's the middle of the night, you should go to bed early")
    if hour >=6 and hour < 12:
        speak("Hi  ,Good morning my friend")
    elif hour >=12 and hour < 18:
        speak("Hi ,Good afternoon my friend")
    if hour >=18 and hour < 24:
        speak("Hi , Good night my friend")
    speak("How can i help you ? ")

def search_wikipedia(query):
    # Search and read the content of a Wikipedia article with the keyword query
    try:
        page = wikipedia.page(query) #retrieve the page
        content = page.content  #store the content of the page in the variable "content" and then use
        speak(content) #read content
    except wikipedia.exceptions.DisambiguationError as e:
        # Error handling in case the query keyword is incorrect
        print(e.options)

def battery():
    battery = psutil.sensors_battery() # get the system battery state and assign it to the variable "battery".
    plugged = battery.power_plugged
    # assign it to the "plugged in" variable. This variable indicates whether the system is plugged in or running on battery power.
    percent = battery.percent #retrieve current battery percentage
    seconds = battery.secsleft #retrieve remaining battery life in seconds

    speak(f'The current battery percentage is {percent}%')
    speak(f'The remaining battery life is {seconds} seconds')


def command():
    c = sr.Recognizer()
    with sr.Microphone() as source: 
        c.pause_threshold = 2 
    # create a microphone object "source" and set the threshold "c.pause_threshold" of silence to 2 seconds.
        audio = c.listen(source)
    #listen to the audio coming from the microphone and assigns it to the variable "audio"
    try:
        query = c.recognize_google(audio, language='vi')
    #uses a try-except block to try to recognize the audio using c.recognize_google(audio, language='vi') 
    #and assigns the recognized text to the variable "query" and print it out with "Me: " prefix.
        print("Me: " + query)
    except sr.UnknownValueError:
        speak("I'm sorry, I didn't understand your question. Please type it out for me.")
        query = str(input("Your order is: "))
    return query



if __name__=="__main__":
    welcome()

    while True:
        query=command().lower()
        if "google"in query:
            speak("What should i search boss ? ")
            search=command().lower()
            url=f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on google')
        if "youtube"in query:
            speak("What should i search boss ? ")
            search=command().lower()
            url=f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on youtube')
        elif "facebook"in query:
            speak("Are you sure ,i think you will have more time to use it ? ")
            search=command().lower()
            url=f"https://www.facebook.com/"
            wb.get().open(url)
        elif "video"in query:
            meme=r"C:\Users\Le Minh Nhat\Downloads\Anh Da Đen - Facebook.mp4"
            os.startfile(meme)
        elif "time" in query:
            time()
        elif "hi" in query:
            speak("Hi,i can hear you , how can i help you ?")
        elif "hello" in query:
            speak("Hi,i can hear you , how can i help you ?")
        elif "where are you from" in query:
            speak("I'm from Ho Chi Minh city , i was created by Minh Nhat")
        elif "wikipedia" in query:
            speak("What should i search boss ? ")
            search=command().lower()
            search_wikipedia(query)
        elif "music" in query:
            music=r"C:\Users\Le Minh Nhat\Downloads\[Vietsub+TikTok] Lan Đình Tự - Châu Kiệt Luân -- 蘭亭序 - 周杰倫.mp4"
            os.startfile(music)
        elif "word" in query:
            word=r"C:\Users\Le Minh Nhat\Desktop\Word.lnk"
            os.startfile(word)
        elif "excel" in query:
            excel=r"C:\Users\Le Minh Nhat\Desktop\Excel.lnk"
            os.startfile(excel)
        elif "visual" in query:
            visual=r"C:\Users\Le Minh Nhat\Desktop\Visual Studio 2022.lnk"
            os.startfile(visual)
            search_wikipedia(query)
        elif "photo"in query:
            #initializes a new video capturer using the default camera (index 0).
            cap = cv2.VideoCapture(0)
            #captures a single frame from the camera and stores it in the variable frame. 
            #The ret variable is a boolean value that indicates whether the frame was successfully captured.
            ret, frame = cap.read()
            #displays the frame in a window with the title "Camera".
            cv2.imshow("Camera", frame)
            #waits for a key press before closing the window and ending the program.
            cv2.waitKey(0)
        elif "good"in query:
            speak("Great, i like that,Do you need me any help today?")
        if "open map"in query:
            speak("What should i search boss ? ")
            search=command().lower()
            url=f"https://www.google.com/maps/place/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on map')
        if "battery"in query:
            battery()
        if "take a computer"in query:
            # Take a screenshot
            screenshot = pyautogui.screenshot()
            # Convert the PIL/Pillow image to an OpenCV image
            screenshot = cv2.cvtColor(numpy.array(screenshot), cv2.COLOR_RGB2BGR)
            # Display the image
            cv2.imshow("Screenshot", screenshot)
            # Wait for a key press
            cv2.waitKey(0)

            
