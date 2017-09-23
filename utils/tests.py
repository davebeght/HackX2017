from HackX2017.utils.api_interface import *
from HackX2017.utils.nlp_utils import *
import numpy as np
import pyaudio
import wave
import scipy.io.wavfile as wavf
import codecs


SAMPLE_TEXT = "Unternehmen in ganz Europa können vorerst aufatmen, die Sorge vor dem „Cliff Edge“-Brexit im März 2019 wäre erstmal gebannt. Doch ist unklar, ob nun wirklich bald die zweite Phase der Brexit-Verhandlungen beginnen kann. Denn zu den drei Kernforderungen der EU blieb May einige Antworten schuldig: Erneut scheute sie davor zurück, die volle Rechnung für den EU-Austritt anzuerkennen. Die liegt laut EU-Kommission bei netto 60 Milliarden Euro. Die Premierministerin versicherte nur, dass Großbritannien alle seine Verpflichtungen erfülle. Über das Ausmaß gibt es weiterhin Streit."

def prepare_test_text(random=False):
  news_articles = handelsblatt_news()
  idx = np.random.randint(len(news_articles)) if random else 0
  return news_articles[idx]['description']



def main():

  #text_analysis()
  text_2_speech()
  #tokenize()



def text_2_speech():
  ''' text 2 speech section '''
  headers = get_headers(type="text2speech")

  # set voice and body settings

  body = ElementTree.Element('speak', version='1.0')
  body.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-us')
  voice = ElementTree.SubElement(body, 'voice')
  voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-US')
  voice.set('{http://www.w3.org/XML/1998/namespace}gender', 'Female')
  voice.set('name', 'Microsoft Server Speech Text to Speech Voice (en-US, ZiraRUS)')
  voice.text = 'This is a demo to call microsoft text to speech service in Python.'

  # Connect to server to synthesize the wave
  print("\nConnect to server to synthesize the wave")
  conn = http.client.HTTPSConnection("speech.platform.bing.com")
  conn.request("POST", "/synthesize", ElementTree.tostring(body), headers)
  response = conn.getresponse()
  print(response.status, response.reason)

  data = response.read()
  conn.close()
  print("The synthesized wave length: %d" % (len(data)))


  play_audio(data)


def text_analysis():
  '''text analysis section'''
  language = detect_language(SAMPLE_TEXT)
  sentiment = detect_sentiment(SAMPLE_TEXT)
  key_phrases = detect_key_phrases(SAMPLE_TEXT)


  print('Text: %s' % SAMPLE_TEXT)
  print('Language: %s' % language)
  print('Sentiment: %f' % sentiment)
  print('Key phrases: %s' % key_phrases)


def tokenize():
  text = prepare_test_text(random=True)
  tokens = tokenize(text)
  print(tokens)


def play_audio(f):
  # instantiate PyAudio
  p = pyaudio.PyAudio()
  # open stream
  stream = p.open(format=p.get_format_from_width(f.getsampwidth()), channels=f.getnchannels(), rate=f.getframerate(),
                  output=True)
  # read data
  data = f.readframes(1024)

  #play stream
  while data:
      stream.write(data)
      data = f.readframes(1024)

  #stop stream
  stream.stop_stream()
  stream.close()

  #close PyAudio
  p.terminate()


if __name__ == "__main__":
  main()