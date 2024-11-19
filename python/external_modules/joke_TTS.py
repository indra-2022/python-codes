import pyjokes
import pyttsx3
def joke():
    joke=pyjokes.get_joke()
    engine = pyttsx3.init()
    print(joke)
    engine.say(joke)
    engine.runAndWait()
while 1 :
    a=int(input("press 1 to start: "))
    if a==1:
        joke()
