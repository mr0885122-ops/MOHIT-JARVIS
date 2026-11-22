
import datetime
import webbrowser

try:
    import pyttsx3
    engine = pyttsx3.init()
except Exception:
    engine = None

def speak(text):
    print("JARVIS:", text)
    if engine:
        engine.say(text)
        engine.runAndWait()

def jarvis():
    speak("Hello Mohit! Main aapka Jarvis hoon.")
    speak("Aap kya karna chahte hain?")

    while True:
        command = input("MOHIT: ").lower().strip()

        if "namaste" in command or "hello" in command:
            speak("Namaste Mohit! Main aapki kya madad kar sakta hoon?")

        elif "time" in command or "समय" in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak("Abhi samay hai " + now)

        elif "date" in command or "तारीख" in command:
            today = datetime.datetime.now().strftime("%d-%m-%Y")
            speak("Aaj ki date hai " + today)

        elif "youtube" in command:
            speak("YouTube khol raha hoon.")
            webbrowser.open("https://www.youtube.com")

        elif "google" in command:
            speak("Google khol raha hoon.")
            webbrowser.open("https://www.google.com")

        elif "बंद" in command or "exit" in command:
            speak("Goodbye Mohit!")
            break

        else:
            speak("Maaf kijiye Mohit, main samajh nahi paya.")

if __name__ == "__main__":
    jarvis()

