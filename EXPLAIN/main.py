import speech_recognition as sr
import pandas as pd
from gtts import gTTS
import pygame
def text_aud():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        text = r.listen(source)
    try:    
        return r.recognize_google(text)
    except:
        return -1
def explain(message):
    myobj = gTTS(text=message, lang='en', slow=False)
    myobj.save("welcome.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("welcome.mp3")
    pygame.mixer.music.play()
topic = str(text_aud())
topic = topic.upper()
lists = pd.read_csv('details.csv', header = None)
for x in range(0,len(lists[0])):
    if lists[0][x] in topic:
        explain(lists[1][x])
