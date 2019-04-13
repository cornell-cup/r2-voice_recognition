import csv
import pandas
df=pandas.read_csv("C:\PythonProjects\\r2-voice_recognition\CSVSentences\sentences.csv",
    converters={"Sentences": str, "Sentiment Value":float, "NLTK Prediction":float, "Watson Prediction":float})
df.to_csv("C:\PythonProjects\\r2-voice_recognition\CSVSentences\sentencesPanda.csv")

with open("C:\PythonProjects\\r2-voice_recognition\CSVSentences\sentencesPanda.csv", newline='', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    nltkCount = 0
    watsonCount = 0
    next(reader)
    for row in reader:
     sentiment = float(row[2])
     print(sentiment)
     nltk = float(row[3])
     watson = float(row[4])
     #print(nltk)
     #print(watson)
     if(sentiment == 1.0):
         if(nltk > 0):
             nltkCount = nltkCount + 1
         if(watson > 0):
             watsonCount = watsonCount + 1
     else:
         if(nltk < 0):
             nltkCount = nltkCount + 1
         if(watson < 0):
             watsonCount = watsonCount + 1

print(nltkCount)
print(float(nltkCount)/3000)
print(watsonCount)
print(float(watsonCount)/3000)