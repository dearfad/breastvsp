import streamlit as st
import speech_recognition as sr


def get_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        mic_status_placeholder = st.empty()
        mic_status_placeholder.info("倾听中...")
        audio = recognizer.listen(source, timeout=None, phrase_time_limit=10)
        mic_status_placeholder.info("语音识别中...")
        asr_message = recognizer.recognize_whisper(
            audio, model="small", language="chinese"
        )
        mic_status_placeholder.empty()
    return asr_message


if __name__ == "__main__":
    while True:
        st.write(get_speech())
