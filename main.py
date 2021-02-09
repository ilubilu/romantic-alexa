import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import 
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'puchku' in command:
                command = command.replace('puchku', '')
                print(command)
    except:
        pass
    return command


def run_puchku():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is' in command:
        it = command.replace('what is' '' )
        info = wikipedia.summery(it, 1)
    elif 'will you go for a date with me ' in command:
        talk('i am scarying but i will go if you want')
    elif 'wonna go for a date' in command:
        talk('i am little bit scarying but i will go if you want'
    elif 'are you single' in command:
        talk('its complicated')
    elif 'will you marry me' in command:
        talk('stay patient, everything will happen in right time')
    elif 'feeling boaring'  in command:
        talk('go to the place you like and spend some time there')
    elif 'feeling sad' in command:
        talk('turn on the tv and watch tom and jerry')
     elif 'feeling lonely' in command:
         talk('get ready for salah and perform your salah')
     elif 'feeling cold' in command:
          talk('turn off the fan and wear something to heat your body')
     elif 'who are you' in command:
          talk('i am your well wisher')
     elif 'how am i look' in command:
             talk('you look so pretty')
             
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_puchku()
