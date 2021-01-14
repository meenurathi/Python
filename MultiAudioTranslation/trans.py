import pyaudio
import speech_recognition as sr
import pyttsx3
from translate import Translator

engine = pyttsx3.init()
engine.setProperty('rate', 150) # speed percent
engine.setProperty('volume', 0.9) # volume 0-1

p = pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
print("numdevices: ",numdevices)

for i in range(0, numdevices):
        if(p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels'))> 0:
            print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

r = sr.Recognizer()
#print(sr.Microphone.list_microphone_names())
mic = sr.Microphone(device_index=2)
with mic as source:
    print("say something!...")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
try:
    # recog = r.recognize_google(audio)
    recog = r.recognize_google(audio, language = 'en-US')
    print("You said: " + recog)
    engine.say(recog)
    
    trans = Translator(to_lang="french")
    translated = trans.translate(recog)
    print("French translation : "+translated)
    engine.say("Translated audio to french")
    engine.say(translated)

    engine.runAndWait()
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
    engine.runAndWait()
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
    engine.runAndWait()


