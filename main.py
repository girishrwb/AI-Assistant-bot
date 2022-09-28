import speech_recognition as sr #importing and give name
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import wolframalpha

client = wolframalpha.Client('app_id')

listener = sr.Recognizer()      #helps recognize/understand wat u want to say
talk = pyttsx3.init()
voices = talk.getProperty('voices')   #fetches all the voices available
talk.setProperty('voice', voices[1].id)  #sets the male voice, 1 for female

def speak(text):        #fn to speak whatever we enter
    talk.say(text)
    talk.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            talk.say("what do u want now???") #it talks to me

            talk.runAndWait()                 #make sure it talks
            print("What do u want now???")

            voice = listener.listen(source)         #listens to my voice
            command = listener.recognize_google(voice)  #recognizes my voice -> speech
            command = command.lower()
            if 'ginger' in command:
                command = command.replace('ginger', '')

            #if 'hello' in command: think of a name that works!!!
            print(command)
            #talk.say(command)           #speaks what i typed
            #talk.runAndWait()
            #speak(command)
    except: pass
    return command

def run_ginger():       #sep fn for controlling the command input
    command = take_command()

    if 'play' in command:
        command = command.replace('play', '')
        #print(command)
        speak('playing')
        print('playing....')
        pywhatkit.playonyt(command)

    elif 'what is your name' in command:
        print("Im ginger!")
        speak("Im ginger!")

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%a %I:%M %p')
        print(time)
        speak("its" + time + "girish")

    elif 'what is' in command:
        subject = command.replace('what is', '')
        info = wikipedia.summary(subject,2)
        print(info)
        speak(info)


    elif 'who is' in command:
        subject = command.replace('who is', '')
        info = wikipedia.summary(subject, 2)
        print(info)
        speak(info)


    elif 'joke' in command:
        joke1 =pyjokes.get_joke()
        print(joke1)
        speak(joke1)
        speak('HAHA, i know that was lame, but i hope your happy')

    elif 'where am i' in command:
        print("home sweet home")
        speak("home sweet home")

    elif 'temperature' in command:   #under dev!!!
        res = client.query(command)
        print(res)
        speak(res)


    else:
        print('say it again')
        speak('say it again, please')

while True:
    run_ginger()


run_ginger() #driver fn

