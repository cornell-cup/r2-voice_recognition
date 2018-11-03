#!/usr/bin/python3

import pyaudio
import speech_recognition as sr

print("\n\n\n\n Microphone names \n\n\n\n")
print(sr.Microphone.list_microphone_names())
print("\n\n\n\n Microphone information \n\n\n\n")
for i in range(pyaudio.PyAudio().get_device_count()):
  print("index " + str(i) + " \n")
  print(pyaudio.PyAudio().get_device_info_by_index(i))
  print("\n")
print("\n\n\n\n")
r = sr.Recognizer()
mic = sr.Microphone(0)
with mic as source:
  r.adjust_for_ambient_noise(source)
  audio = r.listen(source)
print(r.recognize_google(audio))
