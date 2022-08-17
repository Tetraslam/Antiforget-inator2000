import speech_recognition as sr

r = sr.Recognizer()

mic = sr.Microphone()
def addEvent():
  eventname = input("Please provide a name for the event: ")
  eventfile = open(eventname + ".txt", "w+")
  eventcontent = input("Please enter event details: ")
  eventfile.write(eventcontent)

def addMedication():
  medicationname = input("Please enter medication name: ")
  medicationfile = open(medicationname + ".txt", "w+")
  medicationcontent = input("Medication details (volume/number of pills, time to take them)")
  medicationfile.write(medicationcontent)

def main():
  option = input("Add event or medication?")
  if option=="event" or option=="add event":
    with mic as source:
      r.adjust_for_ambient_noise(source)
      audio = r.listen(source)
      speech = r.recognize_google(audio)
      print(speech)
      if speech == "add event" or speech == "add an event" or speech == "new event":
        addEvent()
  elif option=="medication" or option=="add medication":
    with mic as source:
      r.adjust_for_ambient_noise(source)
      audio = r.listen(source)
      speech = r.recognize_google(audio)
      print(speech)
      if speech == "add medication" or speech == "add a medication" or speech == "new medication":
        addMedication()
if __name__=="__main__":
  main()
