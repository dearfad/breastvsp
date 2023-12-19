import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source, timeout=3, phrase_time_limit=5)
    print('recognition')
    message = r.recognize_whisper(audio, model="base", language="chinese")
    return message

if __name__ == "__main__":
    print(listen())