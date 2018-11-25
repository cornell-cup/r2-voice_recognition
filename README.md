# r2-voice_recognition

ABSTRACT:
Ever want a robot to reciprocate your feelings about what you are thinking about? 
What if it is going onto your favorite Star Wars bot? Well, don't look any further. 
It is right here (just in development, of course).

PROJECT DEVELOPMENT: 
   1) Speech Recognition: In the Fall 2018 semester, the development of a minimum viable product (mvp) has been completed with
   a Raspberry PI and a ReSpeaker Microphone. This mvp is equipped with a simple NLTK sentiment analysis algorithm that uses a 
   bag of words model to create a numeric representation of what a user is saying between -1 and 1 (negative to positive).
   Some issues of this model is that it only takes into account the individual words in the sentence, not the connotation of the 
   sentence itself. For example, negation statements such as "not" are not interpreted correctly in statements that, when analyzed, seem
   negative but are actually positive.

   2) Sentiment Analysis Algorithm: to be implemented in Spring 2019 semester



SOURCES USED:
https://www.seeedstudio.com/ReSpeaker-2-Mics-Pi-HAT-p-2874.html - microphone used in creating the MVP
https://github.com/respeaker/respeaker_python_library - used for speech-to-text implementation
https://www.nltk.org/ - used for basic sentiment analysis

