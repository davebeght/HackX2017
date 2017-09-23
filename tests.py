from utils.api_interface import *
from utils.nlp_utils import *
import numpy as np

SAMPLE_TEXT = "Unternehmen in ganz Europa können vorerst aufatmen, die Sorge vor dem „Cliff Edge“-Brexit im März 2019 wäre erstmal gebannt. Doch ist unklar, ob nun wirklich bald die zweite Phase der Brexit-Verhandlungen beginnen kann. Denn zu den drei Kernforderungen der EU blieb May einige Antworten schuldig: Erneut scheute sie davor zurück, die volle Rechnung für den EU-Austritt anzuerkennen. Die liegt laut EU-Kommission bei netto 60 Milliarden Euro. Die Premierministerin versicherte nur, dass Großbritannien alle seine Verpflichtungen erfülle. Über das Ausmaß gibt es weiterhin Streit."

def prepare_test_text(random=False):
  news_articles = handelsblatt_news()
  idx = np.random.randint(len(news_articles)) if random else 0
  return news_articles[idx]['description']



def main():
  language = detect_language(SAMPLE_TEXT)
  sentiment = detect_sentiment(SAMPLE_TEXT)
  key_phrases = detect_key_phrases(SAMPLE_TEXT)


  print('Text: %s' % SAMPLE_TEXT)
  print('Language: %s' % language)
  print('Sentiment: %f' % sentiment)
  print('Key phrases: %s' % key_phrases)


  #text = prepare_test_text(random=True)
  #tokens = tokenize(text)
  #print(tokens)

if __name__ == "__main__":
  main()