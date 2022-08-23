import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes
import tkinter as tk


def run_device():
    listener = sr.Recognizer()

    user_name = 'Godfrey'
    ai_name = 'Mordecai'

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    masculine_voice = voices[0].id
    feminine_voice = voices[1].id

    def intro():
        engine.setProperty('voice', feminine_voice)
        engine.say(f'Hello master {user_name}')
        engine.say('What can I do for you today')
        engine.runAndWait()

    def talk(text):
        engine.say(text)
        engine.runAndWait()

    def take_command():
        try:
            with sr.Microphone() as source:
                print('listening...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)  # audio to text
                command = command.lower()
                if ai_name.lower() in command:
                    command = command.replace(ai_name.lower(), '')
                    print(command)

        except:
            command = ''
        return command

    def run_ai():
        command = take_command()
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'what time is it' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk(f'the time is {time}')
        elif 'what is' in command:
            object = command.replace('what is', '')
            info = wikipedia.summary(object, 1)
            print(info)
            talk(info)

        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)

        elif 'tell me a joke' in command:
            joke = pyjokes.get_joke()
            talk(joke)
            print(joke)
        elif 'find' in command:
            destination = command.replace('find', '')
            talk(f'taking you to {destination}')
            pywhatkit.search(destination)
        else:
            talk("sorry, I don't understand")
            print('this command was not recognized')
            run_ai()

    intro()
    while True:
        run_ai()


root = tk.Tk()
root.title('Jarvis II')
root.geometry('300x300')

btn = tk.Button(root, text='Listen', command=run_device)
btn.pack()

root.mainloop()
