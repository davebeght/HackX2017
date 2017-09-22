



#import modules

import pandas as pd
import os
import numpy as np
from sklearn.pipeline import Pipeline
import nltk
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.decomposition import TruncatedSVD
from sklearn import metrics






from nltk.corpus import brown


from nltk import sent_tokenize, word_tokenize, pos_tag
from sklearn.datasets import fetch_20newsgroups

text = "Machine learning is the science of getting computers to act without being explicitly programmed. In the past decade, machine learning has given us self-driving cars, practical speech recognition, effective web search, and a vastly improved understanding of the human genome. Machine learning is so pervasive today that you probably use it dozens of times a day without knowing it. Many researchers also think it is the best way to make progress towards human-level AI. In this class, you will learn about the most effective machine learning techniques, and gain practice implementing them and getting them to work for yourself. More importantly, you'll learn about not only the theoretical underpinnings of learning, but also gain the practical know-how needed to quickly and powerfully apply these techniques to new problems. Finally, you'll learn about some of Silicon Valley's best practices in innovation as it pertains to machine learning and AI."


sents = sent_tokenize(text)
tokens = word_tokenize(text)




#get data
categories = ['alt.atheism', 'soc.religion.christian',
               'comp.graphics', 'sci.med']


twenty_train = fetch_20newsgroups(subset='train',
    categories=categories, shuffle=True, random_state=42)


#print the first line of loaded files
#print("\n".join(twenty_train.data[0].split("\n")[:3]))



twenty_train.target[:10]


#get target attribute
#print(twenty_train.target_names)

len(twenty_train.data)



#TD-# IDF processing
#count occurence of words
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)

#calculate TDIDF
tfidf_transformer = TfidfTransformer(use_idf= False)
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)



#as a pipeline


#training a classifier
text_clf = Pipeline([('vect', CountVectorizer()),
                      ('tfidf', TfidfTransformer()),
                      #('svd', TruncatedSVD()),
                      ('clf', MultinomialNB()),
 ])


#training a classifier
text_clf.fit(twenty_train.data, twenty_train.target)


	


#evaluation of performance on testset
twenty_test = fetch_20newsgroups(subset='test',
     categories=categories, shuffle=True, random_state=42)
docs_test = twenty_test.data
predicted = text_clf.predict(docs_test)
print('accuracy: ' + str(np.mean(predicted == twenty_test.target)))


print(metrics.classification_report(twenty_test.target, predicted,
     target_names=twenty_test.target_names))