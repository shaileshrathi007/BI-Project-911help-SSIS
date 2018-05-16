import speech_recognition as sr # import speech recognition module 
from os import path
import os
# os.chdir('/media/viraj/New Volume/Work/DWBI/911/audio/High')
print('transcribing')

import logging
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(messafe)s', 
    level=logging.INFO)
import numpy as np
import pandas as pd


# Function to transcribe audio using IBM speech-to-text API.
# Function to transcribe audio using IBM speech-to-text API.
def ibm_stt(audio_file):
    audio_file = path.join(path.dirname(path.realpath(x)), x)
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
    IBM_USERNAME = "d316d45a-bb7f-4ac4-9281-be32017b1e8f"  
    IBM_PASSWORD = "NobzB1XFtB8N"
    text = r.recognize_ibm(audio,username=IBM_USERNAME,password=IBM_PASSWORD)
    file = open("High_good_ibm.txt", "a")
    # y = str(x)
    # file.write(y + "\n" + str(text) + "\n")
    # file.close()
    print(text)
    return 


# def google(x):
#     audio_file = path.join(path.dirname(path.realpath(x)), x)
#     r = sr.Recognizer()
#     with sr.AudioFile(audio_file) as source:
#         audio = r.record(source)
#     GOOGLE_CLOUD_SPEECH_CREDENTIALS = None
#     text = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
#     file = open("High_Good_google.txt", "a")
#     y = str(x)
#     file.write(y + "\n" + str(text) + "\n")
#     file.close()
#     print('File Saved')
#     return     
if __name__ == '__main__':
    os.chdir('/media/viraj/New Volume/Work/DWBI/911/audio/High')
    IBM('4.flac')
    



