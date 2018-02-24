# Importing the libraries
import pandas as pd
import numpy as np
import pygame
import os
from gtts import gTTS
import random

# Importing the dataset
dataset = pd.read_csv('details.csv', header=None)
headings = dataset.iloc[:, 0].values.tolist()
explanations = dataset.iloc[:, 1].values

# Abbreviating the headings
abbr_headings = []
for x in headings:
    abbr = ''.join(x)
    abbr = abbr.split(' ')
    abbre = "" 
    for y in abbr:
        if y != '':
            abbre += y[0]
    abbr_headings.append(abbre)

# Function to convert text to audio and play mp3 file
def audio(message):
    myobj = gTTS(text=message, lang='en', slow=False)
    file_path = "welcome" + str(random.randint(1,101)) + ".mp3"
    myobj.save(file_path)
    pygame.mixer.init(26000)
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# Take user input of string
list_direc = os.listdir()
for x in list_direc:
    if "mp3" in x:
        os.remove(x)
while True:
    details = input("What do you want to know? ")
    if details == "1":
        break
    details = details.upper()
    sorry_message = "Sorry, I do not recognize what you said."
    i = 0
    while i<len(headings):
        if details == headings[i]:
            audio(explanations[i])
            flag = 0
            break
        elif details == abbr_headings[i]:
            audio(explanations[i])
            flag = 0
            break
        else:
            flag = 1
        i += 1
    if flag == 1:
        audio(sorry_message) 
