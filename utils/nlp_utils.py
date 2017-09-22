import nltk

def tokenize(text):
  """
  :param text: string to tokenize
  :return: Array of strings/tokens
  """
  assert type(text) is str
  return nltk.word_tokenize(text)

def pos_tags(text):
  pass