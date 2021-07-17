import speech_recognition as sr
import pyttsx3
import pywhatkit
from datetime import datetime
import wikipedia
import pywhatkit as pw
import os
import time

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

namea = 'sarah'
namey = "Señor Stark"
cels =["father:+541149770791","adoptado:+5491141673005","monkey:+5491132512401"]
exe = ['discord.exe','notepad.exe','chrome.exe','pycharm.exe']

def talk(text):
    engine.say(text)
    engine.runAndWait()

engine.say(f"Hi {namey} I am active by and for you...")
print(f"+Hi {namey} I am active by and for you...")
engine.runAndWait()

def listen():
    '''Escucha lo ingresado por el microfono y se retorna la variable "rec" la cual
    contiene lo ingresado pasado a minuscula. Ademas se dice cuando se esta escuchando
    y que se toma como ingresado con los prints "Escuchando..." y "-Usted dijo: "'''

    rec = ''
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source, duration=0.2)
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            rec = rec.lower()
            print("-You said: "+rec)
    except:
        pass

    return rec

def subrun():
    rec = listen()
    try:
        if 'play' in rec:
            play(rec)

        elif 'triste' in rec:
            triste()

        elif 'date' in rec:
            fecha()

        elif 'time' in rec:
            hora()

        elif 'info' in rec:
            wiki(rec)

        elif 'search' in rec:
            buscar(rec)

        elif 'open' in rec:
            abrir(rec)

        elif 'como se llama dios' in rec:
            talk("My lord and master is called Ignacio Cesarani")
            print("+My lord and master is called Ignacio Cesarani")

        elif 'suicide' in rec:
            suicidio()

        elif 'what is your name' in rec:
            wiyn()

        elif 'shutdown' in rec:
            shutdown()

        elif 'send' in rec:
            send(rec) 

        elif 'exit' in rec:
            exit()
            return False

        elif 'do you love me' in rec:
            amor()


        else:
            print("+Try again")
            talk("Try again")
    except:
        pass

    return True

def run():
    '''Main function where the whole program is carried out'''

    rec = listen()
    rec = rec.replace('sada', 'sarah')
    rec = rec.replace('zara', 'sarah')

    if namea in rec:
        talk(f"Tell me {namey}, what do you need?...")
        print(f"+Tell me {namey}, what do you need?...")

        seguir = True
        cont = 0
        subrun()
        while(cont<7)and(seguir==True):
            seguir = subrun()
            cont=cont+1
        print("+I go to invisible mode, I start again with the command  "+namea)
        talk("I go to invisible mode, I start again with the command  "+namea)

    elif (rec=='exit'):
        exit()
        return jt==False

    return jt==True

def abrir(rec):
    '''Open an application // Usage: one enters "open" and an app that is searched among the list of apps'''

    rec = rec.replace('open', '')
    app = ''
    for k in range(len(exe)):
        aux = exe[k].split('.')
        if aux[0] in rec:
            app = aux[0]+'.'+aux[1]
            break

    os.system("start "+app)



def fecha():
    '''It tells you what date it is // Use: one enters date and Sarah tells you what day it is today'''

    dia = datetime.today()
    dia = dia.strftime("%d/%m/%Y")
    print("+Today is " + dia)
    talk("Today is " + dia)

def hora():
    '''It tells you what time it is // Usage: you enter time and Sarah tells you what time it is currently'''

    tim = datetime.now()
    tim = tim.strftime("%I:%M %p")
    print("+The current time is " + tim)
    talk("The current time is " + tim)

def exit():
    '''The program stops working // Usage: one enters exit and the program exits its infinite while function'''

    print("+See you soon "+namey)
    talk("See you soon "+namey)

def send(rec):
    '''
    A message is sent by wpp to a specific person /// Use: one enters "send (name)"
    The name will define the recipient and then you will be asked to enter
    what text do you want to send'''

    print("+A message will be sent by whatsapp")
    talk("A message will be sent by whatsapp")

    cel = ''

    for k in range(len(cels)):
        aux = cels[k].split(':')
        if aux[0] in rec:
            cel = aux[1]

    if cel != '':
        print(f"+The message will be sent to {cel} What message do you want to send?")
        talk(f"The message will be sent to {cel} What message do you want to send")
        rec = listen()
        print("Your message was: " + rec)
        pw.sendwhatmsg(cel, rec, int(datetime.now().strftime("%H")), int(datetime.now().strftime("%M")) + 1)
    else:
        print("+No recipient was found")
        talk("No recipient was foundo")

def shutdown():
    '''Turn off your PC // Usage: when instructing Sarah to "shutdown" she will ask if she wants to shut down her PC, if she says "yes" to shut down'''


    print("+Are you sure you want to shut down the computer?")
    talk("Are you sure you want to shut down the computer?")
    rec = listen()
    if 'yes' in rec:
        print("+I hope to see you soon "+namey)
        talk("I hope to see you soon "+namey)
        talk("Your PC will shut down")
        time.sleep(2)
        os.system("shutdown /p")
    else:
        print("+PC shutdown has been canceled")
        talk("PC shutdown has been canceled")

def wiyn():
    '''Print her name // Use: ask "what is your name" and the bot will print and use talk to say it'''

    print("+My name is " + namea)
    talk("My name is " + namea)

def play(rec):
    '''
    A video is played in yt // Use: one enters "play (video title)"
    the video that best matches what was entered will be searched and it will be played
    in some search engine'''

    music = rec.replace('play', '')
    talk('Playing' + music)
    print("+Playing")
    pywhatkit.playonyt(music)
    time.sleep(10)

def suicidio():
    '''A joke is made about the bot's self-destruction'''

    print("+I will self-destruct in")
    talk("I will self-destruct in")
    print("+3")
    talk("3")
    time.sleep(1)
    print("+2")
    talk("2")
    time.sleep(1)
    print("+1")
    talk("1")
    time.sleep(1)
    print("+Haha just kidding")
    talk("Haha just kidding")

def triste():
    '''Momento sad para cuando estas triste'''

    print("+Que paso mi rey estas triste?")
    talk("Que paso mi rey estas triste?")
    pywhatkit.playonyt("Kevin Kaarl - Vámonos a Marte [Letra]")
    time.sleep(15)
    print("+Digame don, que sucedio?")
    talk("Digame don, que sucedio?")
    time.sleep(10)
    print("+No estes mal todo se va a solucionar...")
    talk("No estes mal todo se va a solucionar...")
    time.sleep(2)
    print("+*PAUSA DRAMATICA*")
    time.sleep(2)
    print("+...")
    time.sleep(2)
    print("+bueno sigamos")

def buscar(rec):
    '''Search in google what was entered // Use: one enters "search (desired search)" and it will open
    a google page where the entered is searched'''

    buscar = rec.replace('search', '')
    pywhatkit.search(buscar)
    time.sleep(10)

def wiki(rec):
    '''Explain information about what was entered // Use: what is entered in wikipedia is searched and reproduced'''

    order = rec.replace('info', '')
    info = wikipedia.summary(order, 1)
    print(info)
    talk(info)

def amor():
    print("+I do love you "+namey)
    talk("I do love you "+namey)

jt = True
while jt == True:
    jt = run()


