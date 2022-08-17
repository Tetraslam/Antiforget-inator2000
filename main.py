#!/usr/bin/python
# -*- coding: utf-8 -*-
import speech_recognition as sr
import os

# Sets up the recognition class

r = sr.Recognizer()
mic = sr.Microphone()


def addEvent():
    eventname = input('Please provide a name for the event: ')
    eventfile = open(eventname + '.txt', 'w+')
    eventcontent = input('Please enter event details: ')
    eventday = input('Please enter the day of the event: ')
    eventfile.write(eventcontent + '\n' + eventday)


def addMedication():
    medicationname = input('Please enter medication name: ')
    medicationfile = open(medicationname + '.txt', 'w+')
    medicationtime = input('What time of day must they be taken? ')
    medicationcontent = \
        input('Medication details (volume/number of pills, time to take them)'
              )
    medicationfile.write(medicationname + '\n' + medicationtime + '\n'
                         + medicationcontent)


def today():
    files = os.listdir()
    for i in files:
        if i.endswith('.txt'):
            file = open(i)
            lines = file.readlines()
            print(lines[1])


def main():
    run = input('Run program? (yes/no)')

    if run == 'yes':
        with mic as source:

        # Sets up the microphone for audio input

            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            speech = r.recognize_google(audio)

            if speech == 'add event' or speech == 'add an event' \
                or speech == 'new event':
                addEvent()
            elif speech == 'add medication' or speech == 'medication' \
                or speech == 'new medication':

                addMedication()
            elif speech == 'today':

                today()
    else:

        exit()


if __name__ == '__main__':

  # The code runs on a loop allowing the user to make as many changes as they like

    while True:
        main()
