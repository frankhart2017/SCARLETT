import subprocess
import os
import webbrowser
import help_com
from gtts import gTTS
import pygame
import speech_recognition as sr
from threading import Timer
import time
def audio(message):
    myobj = gTTS(text=message, lang='en', slow=False)
    myobj.save("welcome.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("welcome.mp3")
    pygame.mixer.music.play()

def text_aud():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        text = r.listen(source)
    try:    
        return r.recognize_google(text)
    except:
        return -1

def ret_name(usage):
    if(usage != "1"):
        name = input("Enter name of file:")
    else:
        print("Say name of your file: ")
        name = str(text_aud())
    return name

print("Enter your name: ")
welcome = str(text_aud())
welcome = welcome.lower()
if(welcome == "hero" or welcome == "0"):
    message = "Welcome back Siddhartha."
    audio(message)
    print("Say 1 for voice commands: ")
    usage = str(text_aud())
    for x in usage:
        if x=="1":
            usage = "1";
    print(usage)
    os.system('cls')
    while True:
        if(usage != "1"):
            command = input("\nEnter your command please: ")
            command = command.lower()
        else:
            print("Say your voice command: ")
            command = str(text_aud())
            command = command.lower()
        found = 0
        if(command == "help" or command == "?"):
            help_com.help_commands()
        if(command == "xampp"):
            subprocess.Popen(r'explorer /select,"C:\xampp\htdocs"')
            found = 1
        if(command == "html"):
            name = ret_name(usage)
            if(os.path.isfile(name+'.html')):
                print("File exists already")
            else :
                file = open(name+".html","w")
                file.write("<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title></title>\n\t</head>\n\t<body>\n\t</body>\n</html>")
                file.close()
            subprocess.Popen(['C:\Program Files (x86)\Microsoft VS Code\Code.exe',name+'.html'])
            found = 1
        if(command == "php"):
            name = ret_name(usage)
            if(os.path.isfile(name+'.php')):
                print("File exists already")
            else :
                file = open(name+".php","w")
                file.write("<?php\n\n?>\n\n<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title></title>\n\t</head>\n\t<body>\n\t</body>\n</html>")
                file.close()
            subprocess.Popen(['C:\Program Files (x86)\Microsoft VS Code\Code.exe',name+'.php'])
            found = 1
        if(command == "c"):
            name = ret_name(usage)
            if(os.path.isfile(name+".c")):
               print("File exists already")
            else :
               file = open(name+".c","w")
               file.write("#include<stdio.h>\nint main()\n{\n\n\treturn 0;\n}")
               file.close()
            subprocess.Popen(['C:\Program Files (x86)\Dev-Cpp\devcpp.exe',name+'.c'])
            found = 1
        if(command == "cpp" or command == "c++"):
            name = ret_name(usage)
            if(os.path.isfile(name+".cpp")):
               print("File exists already")
            else :
               file = open(name+".cpp","w")
               file.write("#include<iostream>\nusing namespace std;\nint main()\n{\n\n\treturn 0;\n}")
               file.close()
            subprocess.Popen(['C:\Program Files (x86)\Dev-Cpp\devcpp.exe',name+'.cpp'])
            found = 1
        if(command == "web"):
            print("\n1)ECO WEB HOSTING\n2)FACEBOOK\n3)WHATSAPP WEB\n4)GMAIL\n")
            if(usage != "1"):
                ch = int(input("Enter your choice:"))
                url = ["https://ecowebhosting.co.uk","https://facebook.com","https://web.whatsapp.com","https://gmail.com"]
                if(len(url)>ch-1):
                    webbrowser.open(url[ch-1])
                else:
                    print("Incorrect")
            else:
                print("Say name of website: ")
                ch = str(text_aud())
                ch = ch.lower()
                print(ch)
                if(ch == "eco"):
                    url = "https://ecowebhosting.co.uk"
                    webbrowser.open(url)
                elif(ch == "facebook"):
                    url = "https://facebook.com"
                    webbrowser.open(url)
                elif(ch == "whatsapp"):
                    url = "https://web.whatsapp.com"
                    webbrowser.open(url)
                elif(ch == "mail"):
                    url = "https://gmail.com"
                    webbrowser.open(url)
                else:
                    print("Not in the list")
                
        if(command == "bye" or command=="quit" or command=="exit"):
            break
        if(found == 0):
            print("\nCommand not found")
        num = input("\nPress a key....\n")
        os.system('cls')
else:
    message = "Hi I am Scarlet, but I don't know you " + welcome + ". Bye Bye"
    audio(message)
    wait = input("Press any key to leave....")
print("Bye Bye")
