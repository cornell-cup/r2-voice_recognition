#!/usr/bin/python3

import sys
import speech_recognition as sr
import subprocess
from speech_hackathon import Speech

text = ""
keyword = sys.argv[1]
s = Speech()

while not ():
  try:
    r = sr.Recognizer()
    s.record_speech(3, "keyword.wav")
    record = sr.AudioFile("keyword.wav")
    with record as source:
      audio = r.record(source)
  
    text = r.recognize_google(audio)
    if (keyword in text.lower()):
      try:
        p1 = subprocess.Popen("./end_keyword.sh")
        break
      except OSError:
        pass
        break
  except sr.UnknownValueError:
    pass

