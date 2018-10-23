#!/usr/bin/python3

import speech_recognition as sr
import pyttsx3
import subprocess
import pexpect
import string
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as sid
from multiprocessing import Process 

class Speech:
  def __init__(self):
    pass
  
  def record_speech(this, time, audio_file):
    try:
      p1 = subprocess.Popen(["./speech.sh", str(time), audio_file])
      p1.wait()
    except KeyboardInterrupt:
      try:
        p1.terminate()
      except OSError:
        pass
  
  def speak(this, txt):
    engine = pyttsx3.init()
    engine.say(txt)
    engine.runAndWait()
  
  def convert_to_ints(this, txt):
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

  def recognize_text(this, time, audio_file):
    while(True):
      try:
        r = sr.Recognizer()
        this.record_speech(time)
        record = sr.AudioFile(audio_file)
        with record as source:
          audio = r.record(source)
    
        return r.recognize_google(audio)
      except sr.UnknownValueError:
        speak("I could not understand what you said")
        
  def confirm(this):
    while(True):
      speak("Please confirm if this text is okay")
      txt = this.recognize_text(2)
      senti_analyzer = sid()
      score = senti_analyzer.polarity_scores(txt)['compound']
      if score > 0:
        return True
      elif score < 0:
        return False
      else:
        speak("Sorry I didn't understand that")

  def main(this):
    while(True):
      txt = this.recognize_text(0)
      print(txt)
      this.speak("Your recording is as follows")
      this.speak(txt)
      if (confirm()):
        break
      this.speak("Restarting the recording")
  
    convert_to_ints(txt)

