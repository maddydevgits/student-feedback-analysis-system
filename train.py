# import libraries

import pandas as pd
import nltk
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.linear_model import SGDClassifier
import pickle

data=pd.read_csv('trainingdata.csv')
data=data.dropna()

X=data['sentences']
Y=data['sentiments']

# ML -> SL (Supervised), USL (Unsupervised)

# Labelling - Supervised -> 1. Regression (numeric), 2. Classification (class)
# Unlabelled - Unsupervised -> Clustering

def mnb_classifier(): # Multiomial Naive Bayes
    classifier=Pipeline([('vect',CountVectorizer()),('tfidf',TfidfTransformer()),('clf',MultinomialNB())])
    classifier.fit(X,Y)
    #print(classifier.predict(['bad we are unable to understand']))
    #print(classifier.predict(['super excellent job']))
    #print(classifier.predict(['ok good']))
    Y_pred=classifier.predict(X)
    print(accuracy_score(Y,Y_pred))

def svm_classifier(): # Support Vector Machine
    classifier=Pipeline([('vect',CountVectorizer()),('tfidf',TfidfTransformer()),('clf',SGDClassifier())])
    classifier=classifier.fit(X,Y)
    pickle.dump(classifier,open('model.pkl',"wb"))
    Y_pred=classifier.predict(X)
    print(accuracy_score(Y_pred,Y))

svm_classifier()






