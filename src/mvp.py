import speech_recognition as sr
import pyaudio
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as sid
from random import *
import simpleaudio as sa


def main():
	r = sr.Recognizer()

	### opens microphone and takes speech from human to convert to text
	mic = sr.Microphone(2)
	with mic as source:
		r.adjust_for_ambient_noise(source)
		print("\n\n\nYou may begin talking:\n\n\n")
		audio = r.listen(source)

	try:
		### parsing speech to text
		spoken = r.recognize_google(audio)
		print("The following text was said:\n\n" + spoken)

		### use basic NLTK sentiment analysis algo Vader to assess speech
		senti_analyzer = sid().polarity_scores(spoken)['compound']
		print ("On a -1 to 1 scale (< 0 is negative, > 0 is positive, = 0 is neutral), the text is: " + str(senti_analyzer))
		#TODO: change this section to be more specific to perform more specific analysis

    ### sound output
		lead_folder = "/home/pi/r2-voice_recognition/R2FinalSounds/"
		sounds = {"angry":"R2Angry.wav" , "good":"R2Good.wav" , "happy":"R2Happy.wav" , "neutral":"R2Neutral.wav", "sad":"R2Sad.wav"}
		if (senti_analyzer < -0.5):
			play_sound(lead_folder + sounds["angry"])
		elif (senti_analyzer < 0):
			play_sound(lead_folder + sounds["sad"])
		elif (senti_analyzer == 0):
			play_sound(lead_folder + sounds["neutral"])
		elif (senti_analyzer > 0.5):
			play_sound(lead_folder + sounds["happy"])
		else:
			play_sound(lead_folder + sounds["good"])
    #TODO: change and add sounds for more sentiment (after new algorithm has been constructed)

	except sr.UnknownValueError:
		print ("What are you saying?")

### play sound from speakers
def play_sound(file_name):
	wave_obj = sa.WaveObject.from_wave_file(file_name)
	play_obj = wave_obj.play()
	play_obj.wait_done()


main()




