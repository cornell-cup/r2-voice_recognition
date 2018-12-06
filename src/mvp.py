import speech_recognition as sr
import pyaudio
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as sid
from random import *
import simpleaudio as sa
# import client
import socket
import json
import time

no_clue_final = -999
wakeup_final = -2
sleep_final = 2
move_final = 999

HOST = "192.168.4.201"
PORT = 10000

sendSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sendSocket.connect((HOST, PORT))

data = {}
data["r2"] = "-1"

def main():
	r = sr.Recognizer()

	### opens microphone and takes speech from human to convert to text
	mic = sr.Microphone(2)
	
	### wake up call
	while (True):
		spoken_text = listen(r, mic)
		print("The following startup phrase was said:\n" + spoken_text + "\n")
		if ("wakeupdroid" in simplify_text(spoken_text) or "wake-updroid" in simplify_text(spoken_text)):
			print ("awake")
			# file_object_correct = open("data-yes.csv", "a")
			# file_object_wrong = open("data-no.csv", "a")
			# file_object_r2 = open("r2sayings.txt", "a")
			react_with_sound(wakeup_final)
			break
	
	while (True):
		spoken = listen (r, mic)
		print("The following text was said:\n" + spoken + "\n")
		
		# R2 unsure of input
		if (spoken == ""):
			print ("What?")
			react_with_sound(no_clue_final)
		
		# shut down R2
		elif ("sleepdroid" in simplify_text(spoken)):
			print ("sleeping")
			# file_object_correct.close()
			# file_object_wrong.close()
			react_with_sound(sleep_final)
			break
		
		# have R2 take attendance
		#elif ("takeattendancedroid" in simplify_text(spoken)):
		#	print ("checking in - F.R.")
		#	client.main()
			
		# moving R2
		elif (spoken[:4].lower() == "move" or spoken[:4].lower() == "turn" and spoken[len(spoken)-len("droid"):] == "droid"):
			spoken = simplify_text(spoken)
			if (spoken.lower() == "moveforwarddroid"):
				data["r2"] = "fwd"
			elif (spoken.lower() == "movebackwarddroid"):
				data["r2"] = "rvr"
			elif (spoken.lower() == "moveleftdroid" or spoken.lower() == "turnleftdroid"):
				data["r2"] = "left"
			elif (spoken.lower() == "moverightdroid" or spoken.lower() == "turnrightdroid"):
				data["r2"] = "right"
			
			sendSocket.sendall(json.dumps(data).encode())
			play_sound(move_final)
			#time.sleep(0.1)
			#data["r2"] = "-1"
			#sendSocket.sendall(json.dumps(data).encode())
			
		# R2 analyzing speech
		elif (spoken[:5].lower() == "droid"):
		 	#phrase = spoken[6:]
			### use basic NLTK sentiment analysis algo Vader to assess speech
			phrase = spoken
			sentiment_value = sid().polarity_scores(phrase)['compound']
			print ("On a -1 to 1 scale (< 0 is negative, > 0 is positive, = 0 is neutral), the text is: " + str(sentiment_value))
			#TODO: change this section to be more specific to perform more specific analysis
			
			"""
			#write to file
			print ("good? y or n")
			answer = input()
			if (answer == "y"):
				file_object_correct.write (phrase + "," + str(sentiment_value) + "\n")
			elif (answer == "n"):
				file_object_wrong.write (phrase + "," + str(sentiment_value) + "\n")
			"""
			
			### sound output
			react_with_sound(sentiment_value)
			
					
			#TODO: change and add sounds for more sentiment (after new algorithm has been constructed)
		
		
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
	lead_folder = "/home/pi/r2-voice_recognition/R2FinalSounds/"
	sounds = {"wake up":"R2Awake.wav" , "angry":"R2Angry.wav" , "good":"R2Good.wav" , \
	"happy":"R2Happy.wav" , "neutral":"R2Neutral.wav", "sad":"R2Sad.wav", \
	"sleep":"R2Sleep.wav", "no clue":"R2Confused.wav", "move":"R2Move.wav"}
	
	if (sentiment_value == no_clue_final):
		play_sound(lead_folder + sounds["no clue"])
	elif (sentiment_value == wakeup_final):
		play_sound(lead_folder + sounds["wake up"])
	elif (sentiment_value == sleep_final):
		play_sound(lead_folder + sounds["sleep"])
	elif (sentiment_value == move_final)
		play_sound(lead_folder + sounds["move"])
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

def simplify_text(speech_text):
	text_list = speech_text.lower().split(' ')
	new_speech_text = ""
	for text in text_list:
		new_speech_text += text
	return new_speech_text

main()

""" WAYS "R2" IS INTERPRETED
   - R2
   - part 2
   - how to
"""	



