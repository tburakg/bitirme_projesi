# we need pyaudio to get sound from microphone
import pyaudio
import speech_recognition as sr
import webbrowser
import os

r = sr.Recognizer()

# TODO: null deger donunce hata veriyor try except kur
# TODO: key value değeri olarak komutları txt de tut, program üzerinden key value ekle



def kararVer():
    with sr.Microphone(device_index=2) as source:
        print("başka işlem yapmak istiyor musunuz 5 saniyeniz var")
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        karar = r.recognize_google(audio_data)
        print(karar)
    return karar

while True:
    #sr.Microphone.list_microphone_names()  mikrofonun kaçıncı indexteyse onu yaz
    with sr.Microphone(device_index= 2) as source:
        print("You Can Speak")
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        # convert speech to text
        # we can change language with language parameter (default en)
        # tr yaparsak youtube'u aç dediğimizde
        text = r.recognize_google(audio_data)
        print(text)
    query = text.lower()

    if 'open youtube' in query:
        # http eklemezen internet explorer da açıyor
        webbrowser.open("http://youtube.com")
        karar = kararVer()
        if "no" in karar:
            break
        elif "yes" in karar:
            continue

    elif 'open book' in query:
        filePath = "C:/Users/tbura/Dropbox/PC/Desktop/cv5.pdf"
        os.startfile(filePath)

        karar = kararVer()
        if "no" in karar:
            break
        elif "yes" in karar:
            continue

    elif 'open video' in query:
        filePath = "C:/Users/tbura/Dropbox/PC/Desktop/video1.mp4"
        os.startfile(filePath)
        karar = kararVer()
        if "no" in karar:
            break
        elif "yes" in karar:
            continue

    elif 'open image' in query:
        filePath = "C:/Users/tbura/Dropbox/PC/Desktop/image1.jpg"
        os.startfile(filePath)
        karar = kararVer()
        if "no" in karar:
            break
        elif "yes" in karar:
            continue









