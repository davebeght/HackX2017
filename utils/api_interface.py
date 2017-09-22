import requests
import pprint

NEWS_API_KEY = "ea86c64c545f49d28f6b177dafb0610a"


def handelsblatt_news():
  """ API REQUEST  - Handelsblatt
  :returns Array of dicts, each corresponding to a news article
  """
  r = requests.get('https://newsapi.org/v1/articles?source=handelsblatt&sortBy=latest&apiKey=%s' % NEWS_API_KEY).json()
  assert r['status'] == 'ok'
  return r['articles']

