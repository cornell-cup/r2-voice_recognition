import csv
import sys
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as sid
import simpleaudio as sa
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
    import Features, EntitiesOptions, KeywordsOptions, SentimentOptions

naturalLanguageUnderstanding = NaturalLanguageUnderstandingV1(
version='2018-11-16',
iam_apikey='ZpNv1kcHqUvvzupBoxNRa-PvNKf-vbLnL6QLjBZTvHmr')

with open("C:\PythonProjects\\r2-voice_recognition\CSVSentences\sentences.txt", newline='', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\t')
    csvData = []
    for row in reader:
        spoken = row[0]
        sentiment_value = sid().polarity_scores(spoken)['compound']
        print(sentiment_value)
        print(row)
        print(spoken)
        row.append(sentiment_value)
        try: 
         response = naturalLanguageUnderstanding.analyze(
         text = spoken,
         features = Features(
         sentiment = SentimentOptions(document=None, targets = None))).get_result()
         
         parsed_json = json.loads(json.dumps(response, indent=2))
         sentiment = parsed_json['sentiment']
         document = sentiment['document']
         score = document['score']
         sentiment_value = float(score)

        except:
         sentiment_value = -2
        
        row.append(sentiment_value)
        csvData.append(row)
   
with open('sentences.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    headers = ["Sentences", "Sentiment Value", "NLTK Prediction", "Watson Prediction"]
    writer.writerow(headers)
    writer.writerows(csvData)