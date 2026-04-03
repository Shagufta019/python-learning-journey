import pyttsx3
engine = pyttsx3.init()

engine.setProperty('rate', 150)  # default is around 200
engine.setProperty('volume', 0.9)  # 0.0 to 1.0

engine.say("Hello, I am speaking from Python.")
engine.runAndWait()

