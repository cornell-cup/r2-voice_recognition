#!/usr/bin/python3

import speech_recognition as sr
import pyttsx3
import subprocess
import pexpect
import string
import serial
import nltk
import serial
import time
from text_parsing import Text_Parsing
from nltk.sentiment.vader import SentimentIntensityAnalyzer as sid
from multiprocessing import Process 

def main():
  try:
    speak("Hello.. I. am. awake.")
    p1 = subprocess.Popen(["./keyword_match.py", "start recording"])
    p1.wait()
  except (KeyboardInterrupt, OSError):
    speak("Recording. has. started..")
    pass

  try:
    begin()
  except (OSError):
    pass

def begin():
  while(True):
    p1 = subprocess.Popen(["./keyword_match.py", "stop recording"])
    txt = recognize_text(0)
    speak("Your recording has ended.  The text is being processed.")
    txt = txt[0:txt.find("stop recording")]
    txt = Text_Parsing.fix_grammar(txt)
    print(txt)
    speak("Your recording is as follows")
    speak(txt)
    if (confirm()):
      speak("Printing will begin shortly")
      break
    speak("Restarting the recording")

  write_to_arduino(txt)

def recognize_text(time):
  while(True):
    try:
      r = sr.Recognizer()
      record_speech(time, 'recording.wav')
      record = sr.AudioFile('recording.wav')
      with record as source:
        audio = r.record(source)
  
      return r.recognize_google(audio)
    except sr.UnknownValueError:
      speak("I could not understand what you said")
      
def confirm():
  while(True):
    speak("Please confirm if this text is okay")
    txt = recognize_text(2)
    senti_analyzer = sid()
    score = senti_analyzer.polarity_scores(txt)['compound']
    if score > 0:
      return True
    elif score < 0:
      return False
    else:
      speak("Sorry I didn't understand that")

def record_speech(time, audio_file):
  try:
    p1 = subprocess.Popen(["./speech.sh", str(time), audio_file])
    p1.wait()
  except KeyboardInterrupt:
    speak("Recording. has. Ended..")
    try:
      p1.terminate()
    except OSError:
      pass

def speak(txt):
  engine = pyttsx3.init()
  engine.say(txt)
  engine.runAndWait()

def write_to_arduino(txt):
  ser = serial.Serial('/dev/ttyACM2', 9600)
  time.sleep(2)
  ser.write(' '.encode('utf-8'))
  for c in txt:
    ser.write(c.encode('utf-8'))
    time.sleep(20)

def convert_to_ints(txt):
  int_array = []

  for char in txt:
    int_value = -1
    if (ord(char) == 32):
      int_value = 26
    elif (not char.isalpha()):
      continue
    else:
      int_value = ord(char.lower()) - 97 

    int_array.append(int_value)

  print(int_array)
  return int_array


main()
