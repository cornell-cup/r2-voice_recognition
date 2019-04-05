"""
This is the final code structure for the R2D2 project
Cornell Cup Robotics, Spring 2019

File Created by Yanchen Zhan '22 (yz366)
"""

# import respective packages
import sys
#import speech_recognition as sr
#import pyaudio
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as sid
#from random import *
import simpleaudio as sa
import json
#import client
#import socket
#import json
#import time
#from threading import Thread
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
    import Features, EntitiesOptions, KeywordsOptions, SentimentOptions
import retinasdk
apiKey = "ac486a40-3220-11e9-bb65-69ed2d3c7927"
liteClient = retinasdk.LiteClient(apiKey)

naturalLanguageUnderstanding = NaturalLanguageUnderstandingV1(
version='2018-11-16',
iam_apikey='ZpNv1kcHqUvvzupBoxNRa-PvNKf-vbLnL6QLjBZTvHmr')

setup_bool = False
confirmation_final = 1000
no_clue_final = 999
wakeup_final = 998
sleep_final = 997
move_final = 996
attendance_final = 995
		
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
	
	print ("about to play sound...")
	
	lead_folder = "/home/yanchen-zhan/Documents/Cornell-Cup/r2-voice_recognition/Final/R2FinalSounds/"
	#lead_folder = "C:\PythonProjects\\r2-voice_recognition\Final\R2FinalSounds\\"
	sounds = {"confirmation":"R2OK.wav" , "wake up":"R2Awake.wav" , "angry":"R2Angry.wav" , "good":"R2Good.wav" , \
	"happy":"R2Happy.wav" , "neutral":"R2Neutral.wav" , "sad":"R2Sad.wav" , \
	"sleep":"R2Sleep.wav", "no clue":"R2Confused.wav" , "move":"R2Move.wav" , \
	"attendance":"R2Attendance.wav"}
	
	if (sentiment_value == confirmation_final):
		play_sound(lead_folder + sounds["confirmation"])
	elif (sentiment_value == no_clue_final):
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

def stop():
	print ("emergency invoked")
	react_with_sound(sleep_final)
	sys.exit()
	
# have R2 take attendance
def take_attendance():
	print ("checking in - F.R.")
	react_with_sound(attendance_final)
	client.main()	

def wave(methodcnt):
	global setup_bool
	# initial bootup
	if (setup_bool == False or methodcnt == False):
		setup_bool = True
	else:
		print ("waving")
		#react_with_sound(confirmation_final)
	
def greet(methodcnt):
	global setup_bool
	global setup_cnt
	if (setup_bool == False or methodcnt == False):
		setup_bool = True
	else:
		print ("greeting, don't forget to wave")
		#react_with_sound(confirmation_final)

def grab_item(item, methodcnt):
	global setup_bool
	if (setup_bool == False or methodcnt == False):
		setup_bool = True
	else:
		print ("grabbing " + item)
		#react_with_sound (confirmation_final)
	
def main():
	
	methodcnt = False
	
	#test run to see if all r2 functionality working as expected
	fndictGreetingsKeys = {"wave", "hello", "hi", "hey"}
	fndictGetItemsKeys = {"water", "bottle", "stickers"}
	#fndictGetGamesKey = {"None", "rock paper scissors"}
	
	#in formation of dictionaries, all functions being called
	fndictGreetings = {"wave":wave(methodcnt), "hello":greet(methodcnt), "hi":greet(methodcnt), "hey":greet(methodcnt)}
	fndictGetItems = {"water":grab_item("bottle", methodcnt), "bottle":grab_item("bottle", methodcnt), "stickers":grab_item("sticker", methodcnt)}
	#fndictGames = {"game":game("None"), "games":game("None"), "rock paper scissors":game("rock paper scissors")}
	
	methodcnt = True
	
	### opens microphone instance that takes speech from human to convert to text
	#r = sr.Recognizer()
	#mic = sr.Microphone(2)

	# tells R2 to wake up
	while (True):
		spoken_text = input("enter text here: ")
		#spoken_text = listen(r, mic)
		#spoken_text = spoken_text.lower()
		print("The following startup phrase was said:\n" + spoken_text + "\n")

		if ("r2 stop" in spoken_text):
			stop()
		
		if ("hey r2" in spoken_text):
			print ("awake")
			react_with_sound(wakeup_final)
			break
			
	
	# R2 waits to hear what user wants - CHANGE PROMPTS HERE
	while (True):
		
		spoken = input("enter text here 2: ")
		#spoken = simplify_text(listen (r, mic))
		#spoken = spoken.lower()
		print("The following text was said:\n" + spoken + "\n")
		
		if ("r2 stop" in spoken):
			stop()
		
		# R2 unsure of input
		elif (spoken == ""):
			print ("What?")
			react_with_sound(no_clue_final)
		
		#sentiment analysis
			
		#while (not("stop" in spoken) or not("thank you" in spoken)):
		try:
				
			response = naturalLanguageUnderstanding.analyze(
			text=spoken,
			features=Features(
			sentiment=SentimentOptions(document=None, targets=None))).get_result()

			parsed_json = json.loads(json.dumps(response, indent=2))
			sentiment = parsed_json['sentiment']
			document = sentiment['document']
			score = document['score']
			sentiment_value = float(score)
		
		except:
			sentiment_value = sid().polarity_scores(spoken)['compound']
		
		print(sentiment_value)	
		react_with_sound(sentiment_value)

		#parse intents
		#else:
			#sets up array of key words parsed from words spoken
		keywords = liteClient.getKeywords(spoken)
			 
		if ("high five" in spoken):
			keywords.append("high five")
		
		for x in range(0, len(keywords)):
			
			word = keywords[x]
			print (word)
			
			react_with_sound (confirmation_final)
			
			if (word in fndictGreetingsKeys):	
				fndictGreetings[word]
				print ("in fndictGreetingKeys")
		
			elif (word in fndictGetItemsKeys):
				fndictGetItems[word]
				print ("in fndictGetItemsKey")
				break
		
		"""
		#tell R2 to give information about Cornell Cup
		if ("competition" in keywords):
			spit_info()
				
		#tell R2 to open Periscope
		elif ("periscope" in keywords):
			open_periscope()
		
		#tell R2 to play a game
		elif ("rock paper scissors" in keywords or "game" in keywords):
			game("rock paper scissors")
		"""


main()

	
