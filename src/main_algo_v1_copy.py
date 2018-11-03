import speech_recognition as sr
import pyaudio
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as sid
                     
                                         

### opens microphone and takes speech from human to convert to text
spoken = input()

try:
	### parsing speech to text
	
	### use basic NLTK sentiment analysis algo Vader to assess speech
	senti_analyzer = sid()
	print (senti_analyzer.polarity_scores(spoken)['compound'])
	#TODO: change this section to be more specific to perform more specific analysis
    
except sr.UnknownValueError:
	print ("What are you saying?")
	
#TODO: save R2 sound effects to have it respond a certain way based on sentiment analysis




 
