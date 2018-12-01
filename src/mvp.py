import speech_recognition as sr
import pyaudio
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as sid
from random import *
import simpleaudio as sa

no_clue_final = -999
wakeup_final = -2
sleep_final = 2

def main():
	r = sr.Recognizer()

	### opens microphone and takes speech from human to convert to text
	mic = sr.Microphone(2)
	
	### wake up call
	while (True):
		spoken_text = listen(r, mic)
		if (spoken_text.lower() == "wake up droid"):
			react_with_sound(wakeup_final)
			break
	
	while (True):
		spoken = listen (r, mic)
		print("The following text was said:\n\n" + spoken)
		
		if (spoken.lower() == "sleep droid"):
			react_with_sound(sleep_final)
			break;
	
		### use basic NLTK sentiment analysis algo Vader to assess speech
		sentiment_value = sid().polarity_scores(spoken)['compound']
		print ("On a -1 to 1 scale (< 0 is negative, > 0 is positive, = 0 is neutral), the text is: " + str(sentiment_value))
		#TODO: change this section to be more specific to perform more specific analysis
			
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
		react_with_sound(no_clue_final)
		return ""

"""
plays respective sound from speakers
based on sentiment analysis value
"""
def react_with_sound (sentiment_value):
	lead_folder = "/home/pi/r2-voice_recognition/R2FinalSounds/"
	sounds = {"wake up":"R2Awake.wav" , "angry":"R2Angry.wav" , "good":"R2Good.wav" , "happy":"R2Happy.wav" , "neutral":"R2Neutral.wav", "sad":"R2Sad.wav", "sleep":"R2Sleep.wav", "no clue":"R2Clueless.wav"}
	
	if (sentiment_value == no_clue_final):
		play_sound(lead_folder + sounds["no clue"])
	elif (sentiment_value == wakeup_final):
		play_sound(lead_folder + sounds["wake up"])
	elif (sentiment_value == sleep_final):
		play_sound(lead_folder + sounds["sleep"])
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


main()




