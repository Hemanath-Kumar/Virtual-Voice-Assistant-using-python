import random
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime as dt
import wikipedia
import os
import subprocess
import pywhatkit as kit
import flask
import pyautogui as pg
import time
import pywhatkit
from pywhatkit.core import core, exceptions, log
import json
import keyword
import speedtest as sp

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


def audio_text():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening....")
        audio=r.listen(source)

        try:
            voice=r.recognize_google(audio)
            voice=voice.lower()
            print("User command is ",voice)

        except Exception as e:
            print("exception "+str(e))

    return (voice)


def load():
    #This function is used to load the Json file ,to get the detail of contact
    with open('data/contact.json','r') as f:
       i = json.load(f)
       return i


def contact_detail(): #This function used to add the contact detail in data format .
    m=load()

    while True:
        choice= int(input("1.Add New Contact\n2: Search Contact\n3:Display Contact\n4:Edit Contact\n5: Delete Contact\n6:Exit\nEnter your choice by number : "))
        if choice==1:
            name = input("Enter the contact name = ")
            phone= input("Enter the mobile number = ")
            m[name]=phone

        elif choice == 2:
            search_name = input("Enter the contact name = ")
            if search_name in m:
                print(search_name,"contact number is ",m[search_name])
            else:
                print("Name is not found in contact")


        elif choice == 3:
            #print("Name\tContact Number")
            for key in m:
                print(f"{key}\t\t\t{m.get(key)}")
            break

        elif choice == 4:
            edit_contact =input("Enter the contact name to be edited =")
            if edit_contact in m:
                phone=input("Enter the mobile number to change = ")
                m[edit_contact]=phone
                print("contact updated")
            else:
                print("Name is not found in contact number")

        elif choice ==5:
            del_contact=input("Enter the contact to delete = ")
            if del_contact in m:
                confirm = input("Do you really want to press yes & no =")
                if confirm == 'yes':
                    m.pop(del_contact)
                else:
                    print("Name is not found in contact")
        else:
            break
    #This function used to save the json file in pc.
    with open('data/contact.json', 'w') as f:
        json.dump(m, f)

    m=load()


def whatapp_speak(): #This function used to send whatsapp message throught desktop web.

     n=load()

     speak("Tell me the person name to send message")

     user_audio= audio_text()

     speak('Now,tell me the message')

     message= audio_text()
     
     if user_audio in n and message:

         i=n.get(user_audio)

         webbrowser.open(f"https://web.whatsapp.com/send?phone={i}&text={message}")
         click()

     else:
         print(speak('We have problem to  find the detail of this person\n'
               'Can you use enter detail manually'))

         Name = input('Enter the name of the person = ' + '')

         Message_Text = input('Enter the message = ' + '')

         if Name in n and Message_Text:
             i=n.get(Name)
             webbrowser.open(f"https://web.whatsapp.com/send?phone={i}&text={Message_Text}")
             click()


         else:
             print('* We dont have the detail of this person\n'
                   '* If you want to add new person ?\n'
                   '* Just call open contact ')




def rock():

    speak("watch the screen rules will show ")
    # User to Know the rule below :-
    print("[RULE TO PLAY ROCK PAPER SCISSOR:]\n"
          + "[ Rock vs Paper => Paper - win ]\n"
          + "[ Paper  vs Scissor => Scisoor - win ]\n"
          + "[ Rock vs Scissor =>Rock - Win ]\n")

    print("Enter Your Choice in computer  \n 1.Rock \n 2.Paper \n 3.Scissor\n")

    user = int(input('Enter your Choice between [ 1 TO 3 ] = '))

    for x in range(user):
        if (user < 1 or 3 < user):
            print(f" user choice {[user]} is invaild ")
            break

    bot = "My turn......\n"

    if (user == 1):

        choice = 'user Choice is Rock [1]\n'
        print(choice)
        print(bot)

    elif (user == 2):

        choice = 'user Choice is Paper [2]\n'
        print(choice)
        print(bot)

    elif (user == 3):

        choice = 'user Choice is Scissor [3]\n'
        print(choice)
        print(bot)

    # random.randint is used get to random value from computer

    comp_choice = random.randint(1, 3)

    # This statement used to get computer choice

    if (comp_choice == 1):

        choice_2 = 'AI Choice is Rock [1]\n'

        print(choice_2)

    elif (comp_choice == 2):

        choice_2 = 'AI Choice is Paper[2]\n'

        print(choice_2)

    elif (comp_choice == 3):

        choice_2 = 'AI Choice is Scissor [3]\n'

        print(choice_2)

    print('User VS AI\n')

    # This statement used to find  who is winner!!

    if (user == comp_choice):

        print('Match Is Tie')

    elif (user == 1 and comp_choice == 3 or user == 2 and comp_choice == 1 or user == 3 and comp_choice == 2):

        print(speak('You won the match'))

    elif (user == 1 and comp_choice == 2 or user == 2 and comp_choice == 3 or user == 3 and comp_choice == 1):

        print(Speak('I am Won the match ... '))


def date():
    today=dt.date.today()
    print('Date = ',today.strftime('%A-%d-%B-%Y'))
    speak(today.strftime('%A %d %B %Y'))


def time():
    time=dt.datetime.now()
    print('Time =',time.strftime('%I-%M-%p'))
    speak(time.strftime('%I %M-%p'))

def speedtest():
    test=sp.Speedtest()

    print("Loading server list..")
    test.get_servers() #To get list of server

    print("Loading best server.. ")
    best_server=test.get_best_server() # To get best server to start testing
    print(f"Found - {best_server['host']} located in{best_server['country']}  ")

    print("performing download test...")
    download=test.download() #Use to get result of download speed

    print("performing upoad test...")
    upload=test.upload() #Use to get result of Upload speed

    print("performing ping test...")
    ping=test.results.ping #Use to get result of ping speed

    print(f'Download speed - {download / 1024/1024:.2f} MB/Sec')  #We convert bit per sec result to megabyte per sec
    print(f'Upload speed - {upload/ 1024/1024:.2f} MB/Sec ')
    print(f'Ping - {ping}')


def welcome():
    speak("I am your desktop assistant Lisa! "
          "may I help you")


def lisa():
    welcome()
    query= audio_text()

    if "open youtube" in query:
        webbrowser.open('youtube.com')

    elif 'tell me the time' in query:
        time()

    elif 'play song' in query:
        song=query.replace('play','')
        speak('playing'+song)
        kit.playonyt(song)

    elif 'open spotify' in query:
        speak('opening spotify')
        subprocess.call('C:\\Users\\heamr\\AppData\\Roaming\\Spotify\\Spotify.exe')

    elif 'search'  in query:
        search=query.replace('search','')
        speak('searching'+search)
        kit.search(search)

    elif 'send a whatsapp message' in query:
        whatapp_speak()

    elif 'open whatsapp' in query:
        speak("you want to send a message in whatsapp or i just open the whatsapp for you ?")

        if audio_text() == 'i want to send a message'  or  'send a whatsapp message' :
            whatapp_speak()

        else:
            speak("OK! Opening whatsapp")
            webbrowser.open('https://web.whatsapp.com/')

    elif'open contact' in query:
       # speak("Voice assistant not work in this option")
        contact_detail()

    elif 'play game' in query:
        print(speak("ok,can we play rock,paper,scissor"
              "Just tell me  OK !!!"))
        if audio_text() =='ok':
            rock()
        else:
            speak("OK,we play later")

    elif 'tell me the date' in query:
        date()

    elif "check my internet speed" in query:
        speedtest()

    elif 'bye' in query:
        speak("Bye. Check Out GFG for more exicting things")
        exit()


if __name__ == '__main__':
   lisa()