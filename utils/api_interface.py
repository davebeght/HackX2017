import requests
import pprint

NEWS_API_KEY = "ea86c64c545f49d28f6b177dafb0610a"

# Configure API access
API_KEY = 'b7df04d62fbd48dd974eda12b58ee691'



# Prepare headers
headers = {}
headers['Ocp-Apim-Subscription-Key'] = API_KEY
headers['Content-Type'] = 'application/json'
headers['Accept'] = 'application/json'

def get_headers():
  return headers


def get_api_key():
  return API_KEY



def handelsblatt_news():
  """ API REQUEST  - Handelsblatt
  :returns Array of dicts, each corresponding to a news article
  """
  r = requests.get('https://newsapi.org/v1/articles?source=handelsblatt&sortBy=latest&apiKey=%s' % NEWS_API_KEY).json()
  assert r['status'] == 'ok'
  return r['articles']

