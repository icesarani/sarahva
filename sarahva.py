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
engine.setProperty('voice', voices[1].id)

namea = 'sarah'
namey = "Señor Stark"

def talk(text):
    engine.say(text)
    engine.runAndWait()

engine.say(f"Buenos días {namey} ya estoy activa por y para usted...")
print(f"+Buenos días {namey} ya estoy activa por y para usted...")
engine.runAndWait()

def listen():
    '''Escucha lo ingresado por el microfono y se retorna la variable "rec" la cual
    contiene lo ingresado pasado a minuscula. Ademas se dice cuando se esta escuchando
    y que se toma como ingresado con los prints "Escuchando..." y "-Usted dijo: "'''

    rec = ''
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='en')
            rec = rec.lower()
            print("-Usted dijo: "+rec)
    except:
        pass

    return rec

def run():
    '''Funcion principal donde se lleva adelante todo el programa'''

    rec = listen()
    if namea in rec:
        talk(f"Digame {namey}, que necesita...")
        print(f"+Digame {namey}, que necesita...")
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

            elif 'como se llama dios' in rec:
                talk("Mi amo y señor se llama Ignacio Cesarani")
                print("+Mi amo y señor se llama Ignacio Cesarani")

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
                return jt==False


            else:
                print("+Vuelva a intentarlo")
                talk("Vuelva a intentarlo")
        except:
            pass

    return jt==True

def fecha():
    '''Te dice que fecha es // Uso: uno ingresa date y Sarah te dice que dia es hoy'''

    dia = datetime.today()
    dia = dia.strftime("%d/%m/%Y")
    print("+Hoy es " + dia)
    talk("Hoy es " + dia)

def hora():
    '''Te dice que hora es // Uso: uno ingresa time y Sarah te dice que hora es actualmente'''

    tim = datetime.now()
    tim = tim.strftime("%I:%M %p")
    print("+La hora actual es " + tim)
    talk("La hora actual es " + tim)

def exit():
    '''Deja de funcionar el programa // Uso: uno ingresa exit y el programa se sale de su while infinito de funcion'''

    print("+Nos vemos pronto "+namey)
    talk("Nos vemos pronto "+namey)

def send(rec):
    '''Se envia un mensaje por wpp a una persona en especifico /// Uso: uno ingresa "send (nombre)"
    el nombre definira el destinatario y luego se pedira ingresar
    que texto desea enviar'''

    print("+Se enviara un mensaje por whatsapp")
    talk("Se enviara un mensaje por whatsapp")
    if 'monkey' in rec:
        cel = "+5491132512401"
    elif 'adoptado' in rec:
        cel = "+5491141673005"
    elif 'papa' in rec:
        cel = "+541149770791"

    if cel != '':
        print(f"+Se le enviara el mensaje a {cel} que mensaje desea enviar?")
        talk(f"Se le enviara el mensaje a {cel} que mensaje desea enviar?")
        rec = listen()
        print("Tu mensaje fue: " + rec)
        pw.sendwhatmsg(cel, rec, int(datetime.now().strftime("%H")), int(datetime.now().strftime("%M")) + 1)

def shutdown():
    '''Apaga su PC // Uso: al instruirle "shutdown" a Sarah se te preguntara si desea apagar su PC, si dice "si" se apagara'''


    print("+Esta seguro de que desea apagar la computadora?")
    talk("Esta seguro de que desea apagar la computadora?")
    rec = listen()
    if 'si' in rec:
        print("+Espero verlo dentro de poco "+namey)
        talk("Espero verlo dentro de poco "+namey)
        talk("Se apagara su PC")
        time.sleep(2)
        os.system("shutdown /p")
    else:
        print("+Se ha ancelado el apagado de pc")
        talk("Se ha cancelado el apagado de pc")

def wiyn():
    '''Printea su nombre // Uso: preguntar "what is your name" y el bot printeara y usara de talk para decirlo'''

    print("+Mi nombre es " + namea)
    talk("Mi nombre es " + namea)

def play(rec):
    '''Se reproduce un video en yt // Uso: uno ingresa "play (titulo video)"
    se buscara el video màs acorde a lo ingresado y se reproducira
    en algun buscador'''

    music = rec.replace('play', '')
    talk('Reproduciendo' + music)
    print("+Reproduciendo")
    pywhatkit.playonyt(music)
    time.sleep(10)

def suicidio():
    '''Se hace una broma sobre la autodestruccion del bot'''

    print("+Me autodestruire en")
    talk("Me autodestruire en")
    print("+3")
    talk("3")
    time.sleep(1)
    print("+2")
    talk("2")
    time.sleep(1)
    print("+1")
    talk("1")
    time.sleep(1)
    print("+Jaja es broma")
    talk("Ja ja es broma")

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

def buscat(rec):
    '''Busca en google lo ingresado // Uso: uno ingresa "search (busqueda deseada)" y se abrira
    una pagina de google donde se busca lo ingresado'''

    buscar = rec.replace('search', '')
    pywhatkit.search(buscar)
    time.sleep(10)

def wiki(rec):
    '''Explica informacion sobre lo ingresado // Uso: se busca y reproduce lo ingresado en wikipedia'''

    order = rec.replace('info', '')
    info = wikipedia.summary(order, 1)
    print(info)
    talk(info)

jt = True
while jt == True:
    jt = run()


