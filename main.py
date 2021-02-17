import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


#init voice controller
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'bob' in command:
                command = command.replace('bob', '')
                print(command)
    except:
        pass
    return command

def run_bob():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('The current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'what is' in command:
        item = command.replace('what is', '')
        info = wikipedia.summary(item, 2)
        print(info)
        talk(info)
    elif 'are you single' in command:
        talk('I am in a relationship with your computer')
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)
        print(joke)
    elif 'hello' in command:
        talk('hello! Can I help?')
    elif 'bye' in command:
        talk('have a good day')
    else:
        talk('Sorry I did not understand, please try again.')

while True:
    run_bob()