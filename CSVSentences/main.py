# import respective packages
import sys
#import speech_recognition as sr
#import pyaudio
import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
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

naturalLanguageUnderstanding = NaturalLanguageUnderstandingV1(
version='2018-11-16',
iam_apikey='ZpNv1kcHqUvvzupBoxNRa-PvNKf-vbLnL6QLjBZTvHmr')

import csv
with open("sentences.txt", newline='', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\t')
    csvData = []
    for row in reader:
        spoken = row[0]
        sentiment_value = sid().polarity_scores(spoken)['compound']
        print(sentiment_value)
        row.append(sentiment_value)
        print(row)
        print(spoken)
        csvData.append(row)
   
with open('sentences.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    headers = ["Sentences", "Sentiment Value", "NLTK Prediction"]
    writer.writerow(headers)
    writer.writerows(csvData)