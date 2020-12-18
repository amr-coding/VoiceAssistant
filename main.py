import speech_recognition as sr
import pywhatkit as wk
import time

r = sr.Recognizer()
with sr.Microphone() as source:
    def voiceListen():
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
            voice = r.recognize_google(audio)
            voice = voice.lower()
            r.adjust_for_ambient_noise(source)


        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            print("You said " + voice)
            # wk.playonyt(voice)
        except:
            pass
        return voice


def search():
        voice = voiceListen()
        if 'play' in voice:
            play = voice.replace('play', '')
            wk.playonyt(play)
        elif 'google' in voice:
            voice = voice.replace('google', '')
            wk.search(voice)
        elif 'about' in voice:
            about = voice.replace('info', '')
            rs = wk.info(voice, 3)
        elif 'create' in voice:
            create = voice.replace('create', '')
            f = open(create+'.php', 'x')
            f.close()
        elif 'hey phantom' in voice:
            reply =  voice.replace('hey phantom', '')
            print('how can I help you?')


while True:
    search()

