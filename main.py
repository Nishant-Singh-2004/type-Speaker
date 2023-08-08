import pyttsx3
if __name__ == '__main__':
    print("Welcome to TypeSpeaker,  Created by Nishant")
    txt_speech = pyttsx3.init()
    while True:
        x = input("Enter what you want me to say : ")
        if x == "q":
            txt_speech.say("'bye bye buddy'")
            txt_speech.runAndWait()
            break
        txt_speech.say(x)
        txt_speech.runAndWait()
