import nltk
import json
import urllib.request
from .api_interface import *
import pandas as pd
import os
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.decomposition import TruncatedSVD
from sklearn import metrics


sentimentUri = 'https://westeurope.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment'
languageUri = 'https://westeurope.api.cognitive.microsoft.com/text/analytics/v2.0/languages'
keyPhrasesUri = 'https://westeurope.api.cognitive.microsoft.com/text/analytics/v2.0/keyPhrases'
speechURI = "https://speech.platform.bing.com/synthesize"


def tokenize(text):
  """
  :param text: string to tokenize
  :return: Array of strings/tokens
  """
  assert type(text) is str
  return nltk.word_tokenize(text)


def detect_language(text):
  headers = get_headers()
  postData1 = json.dumps({"documents": [{"id": "1", "text": text}]}).encode('utf-8')
  request1 = urllib.request.Request(languageUri, postData1, headers)
  response1 = urllib.request.urlopen(request1)
  response1json = json.loads(response1.read().decode('utf-8'))
  return response1json['documents'][0]['detectedLanguages'][0]['iso6391Name']


def detect_sentiment(text):
  headers = get_headers()
  language = detect_language(text)
  postData2 = json.dumps({"documents": [{"id": "1", "language": language, "text": text}]}).encode('utf-8')
  request2 = urllib.request.Request(sentimentUri, postData2, headers)
  response2 = urllib.request.urlopen(request2)
  response2json = json.loads(response2.read().decode('utf-8'))
  return response2json['documents'][0]['score']


def detect_key_phrases(text):
  headers = get_headers()
  language = detect_language(text)
  postData3 = json.dumps({"documents": [{"id": "1", "language": language, "text": text}]}).encode('utf-8')
  request3 = urllib.request.Request(keyPhrasesUri, postData3, headers)
  response3 = urllib.request.urlopen(request3)
  response3json = json.loads(response3.read().decode('utf-8'))
  return response3json['documents'][0]['keyPhrases']


def text_to_speech(text):
  ''' text 2 speech section '''
  headers = get_headers(type="text2speech")
  # set voice and body settings
  body = ElementTree.Element('speak', version='1.0')
  body.set('{http://www.w3.org/XML/1998/namespace}lang', 'de-de')
  voice = ElementTree.SubElement(body, 'voice')
  voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'de-DE')
  voice.set('{http://www.w3.org/XML/1998/namespace}gender', 'Female')
  voice.set('name', 'Microsoft Server Speech Text to Speech Voice (de-DE, HeddaRUS)')
  voice.text = text

  # Connect to server to synthesize the wave
  print("\nConnect to server to synthesize the wave")
  conn = http.client.HTTPSConnection("speech.platform.bing.com")
  conn.request("POST", "/synthesize", ElementTree.tostring(body), headers)
  response = conn.getresponse()
  print(response.status, response.reason)
  speech = response.read()
  conn.close()
  print("The synthesized wave length: %d" % (len(speech)))
  return speech



def pos_tags(text):
  pass