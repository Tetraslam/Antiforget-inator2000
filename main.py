import speech_recognition as sr

r = sr.Recognizer()

mic = sr.Microphone()
def addEvent():
  eventname = input("Please provide a name for the event: ")
  eventfile = open(eventname + ".txt", "w+")
  eventcontent = input("Please enter event details: ")
  eventfile.write(eventcontent)
  
def main():
  with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    speech = r.recognize_google(audio)
    print(speech)
    if speech == "add event" or speech == "add an event" or speech == "new event":
      addEvent()

if __name__=="__main__":
  main()
