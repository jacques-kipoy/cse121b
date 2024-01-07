import speech_recognition as sr

# initialize the recognizer
r = sr.Recognizer()

# use the microphone as source
with sr.Microphone() as source:
    print("Speak something...")
    audio = r.listen(source)

try:
    # recognize speech using Google Speech Recognition
    text = r.recognize_google(audio)
    print(f"You said: {text}")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
