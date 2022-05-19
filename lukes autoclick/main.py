import keyboard
import speech_recognition as sr
import os

myvar = 1
in_word = 'auto clicker'
keyword = 'start auto clicker'
endword = 'stop auto clicker'

r = sr.Recognizer()

while myvar == 1:
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)

            print("lisening...")
            audio2 = r.listen(source2)

            MyText = "reset"

            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            if in_word in MyText:
                if keyword in MyText:
                    os.system("start autoclicker.exe")
                    print("started")
                if endword in MyText:
                    os.system('TASKKILL /IM autoclicker.exe /F')
                    print("ended")
    except Exception as e:
                pass