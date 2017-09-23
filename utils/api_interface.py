import requests
import pprint
import http.client, urllib.parse, json
from xml.etree import ElementTree

NEWS_API_KEY = "ea86c64c545f49d28f6b177dafb0610a"

# Configure API access
API_KEY_TEXT_ANALYSIS = 'b7df04d62fbd48dd974eda12b58ee691'
API_KEY_TEXT2SPEECH = 'a0d50c0d4036470ea42b38ab9f526008'


AccessTokenHost = "api.cognitive.microsoft.com"
path = "/sts/v1.0/issueToken"
params = ""


def get_headers(type="text_analysis"):
  headers = {}
  if type == "text_analysis":
    headers['Ocp-Apim-Subscription-Key'] = API_KEY_TEXT_ANALYSIS
    headers['Content-Type'] = 'application/json'
    headers['Accept'] = 'application/json'
  elif type =="text2speech":
    # connect to the server to get the access token
    headers['Ocp-Apim-Subscription-Key'] = API_KEY_TEXT2SPEECH
    access_token = get_access_token(headers)

    headers['Content-Type'] = 'application/ssml+xml'
    headers['Host'] = 'speech.platform.bing.com'
    headers['X-Microsoft-OutputFormat'] = 'riff-16khz-16bit-mono-pcm'
    headers['Authorization'] = 'Bearer ' + access_token
    headers["X-Search-AppId"] = "6bea9009055b4182be1080acd3f7fa2f"
    headers["X-Search-ClientID"] = "f185ab4bbbb54f63989a648fc5f41e94"
    headers["User-Agent"] = "TTSForPython"


  return headers


def get_access_token(headers):
  # Connect to server to get the Access Token
  print("Connect to server to get the Access Token")
  conn = http.client.HTTPSConnection(AccessTokenHost)
  conn.request("POST", path, params, headers)
  response = conn.getresponse()
  print(response.status, response.reason)
  data = response.read()
  conn.close()
  accesstoken = data.decode("UTF-8")
  print("Access Token: " + accesstoken)

  return accesstoken


def get_text_analysis_api_key():
  return API_KEY_TEXT_ANALYSIS


def get_text_2_speech_api_key():
  return API_KEY_TEXT2SPEECH


def handelsblatt_news():
  """ API REQUEST  - Handelsblatt
  :returns Array of dicts, each corresponding to a news article
  """
  r = requests.get('https://newsapi.org/v1/articles?source=handelsblatt&sortBy=latest&apiKey=%s' % NEWS_API_KEY).json()
  assert r['status'] == 'ok'
  return r['articles']

