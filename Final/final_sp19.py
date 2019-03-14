"""
This is the final code structure for the R2D2 project
Cornell Cup Robotics, Spring 2019

File Created by Yanchen Zhan '22 (yz366)

"""

# import respective packages
import speech_recognition as sr
import pyaudio
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as sid
from random import *
import simpleaudio as sa
import client
import socket
import json
import time
from threading import Thread


### opens microphone instance that takes speech from human to convert to text
	r = sr.Recognizer()
	mic = sr.Microphone(2)

	# tells R2 to wake up
	while (True):
		spoken_text = listen(r, mic)
		print("The following startup phrase was said:\n" + spoken_text + "\n")
		
		if ("Hey R2" in spoken_text):
			print ("awake")
			react_with_sound(wakeup_final)
			break
	
	# R2 waits to hear what user wants - CHANGE PROMPTS HERE
	while (True):
		spoken = simplify_text(listen (r, mic))
		print("The following text was said:\n" + spoken + "\n")

		# R2 unsure of input
		if (spoken == ""):
			print ("What?")
			react_with_sound(no_clue_final)
		
		# shut down R2
		elif ("sleepdroid" in spoken):
			print ("sleeping")
			react_with_sound(sleep_final)
			break
		
		# moving R2
        elif (("move" in spoken or "turn" in spoken) and "droid" in spoken):
			moveR2(spoken)
		
		# have R2 take attendance
		elif ("takeattendancedroid" in spoken):
			take_attendance()
		
		# have R2 react to user speech
		

"""
listen to user statement in mic
returns spoken words from user OR 
returns empty string if source not detected
"""
def listen(r, mic):
	with mic as source:
		r.adjust_for_ambient_noise(source)
		print("\n\n\nYou may begin talking:\n\n\n") #testing
		audio = r.listen(source)

	try:
		return r.recognize_google(audio)

	except sr.UnknownValueError:
		print ("What are you saying?") #testing
		return ""


"""
plays respective sound from speakers
based on sentiment analysis value
"""
def react_with_sound (sentiment_value):
	lead_folder = "/home/pi/r2-voice_recognition/Final/R2FinalSounds/"
	sounds = {"wake up":"R2Awake.wav" , "angry":"R2Angry.wav" , "good":"R2Good.wav" , \
	"happy":"R2Happy.wav" , "neutral":"R2Neutral.wav", "sad":"R2Sad.wav", \
	"sleep":"R2Sleep.wav", "no clue":"R2Confused.wav", "move":"R2Move.wav", \
	"attendance":"R2Attendance.wav"}

	if (sentiment_value == no_clue_final):
		play_sound(lead_folder + sounds["no clue"])
	elif (sentiment_value == wakeup_final):
		play_sound(lead_folder + sounds["wake up"])
	elif (sentiment_value == sleep_final):
		play_sound(lead_folder + sounds["sleep"])
	elif (sentiment_value == move_final):
		play_sound(lead_folder + sounds["move"])
	elif (sentiment_value == attendance_final):
		play_sound(lead_folder + sounds["attendance"])
	elif (sentiment_value < -0.5):
		play_sound(lead_folder + sounds["angry"])
	elif (sentiment_value < 0):
		play_sound(lead_folder + sounds["sad"])
	elif (sentiment_value == 0):
		play_sound(lead_folder + sounds["neutral"])
	elif (sentiment_value > 0.5):
		play_sound(lead_folder + sounds["happy"])
	else:
		play_sound(lead_folder + sounds["good"])

### play sound from speakers
def play_sound(file_name):
	wave_obj = sa.WaveObject.from_wave_file(file_name)
	play_obj = wave_obj.play()
	play_obj.wait_done()

# move R2
def moveR2 (spoken):
	global data
	
	# moving R2 forward
	if (spoken.lower() == "moveforwarddroid" or spoken.lower() == "moveforwardsdroid"):
			data = "1"
			#data["r2"] = "fwd"
			
	# moving R2 backward
	elif (spoken.lower() == "movebackwarddroid" or spoken.lower() == "movebackwardsdroid"):
			data = "2"
			#data["r2"] = "rvr"
			
	# turning R2 90deg counterclockwise
	elif (spoken.lower() == "moveleftdroid" or spoken.lower() == "turnleftdroid"):
			data = "3"
			#data["r2"] = "left"
	
	# turning R2 90deg clockwise
	elif (spoken.lower() == "moverightdroid" or spoken.lower() == "turnrightdroid"):
			data = "4"
			#data["r2"] = "right"

	print(data)
	react_with_sound(move_final)


# have R2 take attendance
def take_attendance():
	print ("checking in - F.R.")
	react_with_sound(attendance_final)
	client.main()	


main()

	
