# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 21:07:38 2014

@author: Class2014
"""
import pandas as pd
import numpy as np
#nltk.download()
from nltk.corpus import stopwords
import nltk, os, string
from collections import Counter

os.chdir('C:\\codeforgood')
os.getcwd()

#read csv and change column names
df = pd.read_csv("Email-Content.csv")
df.columns=['score', 'content']

exclude = set(string.punctuation)

#clean messages of html, store in 'clean_message'
df['clean_content'] = [nltk.clean_html(df['content'][i].lower()) for i in range(len(df['content']))]
df['no_stopwords'] = ""
for i in range(len(df['content'])):
    no_stopwords = [w.lower() for w in df['clean_content'][i].split() if not w in stopwords.words('english')]
    filtered_words = []    
    for word in no_stopwords:
        filtered_words.append(''.join([ch for ch in word if ch not in exclude]))
    df['no_stopwords'][i] = ' '.join(filtered_words)

df['freq'] = ""
for i in range(len(df['content'])):
    df['freq'][i] = Counter(df['no_stopwords'][i].split())

df['num_words'] = ""
for i in range(len(df['content'])):
    df['num_words'][i] = len(df['no_stopwords'][i].split())
    
########################### PROCESS THE CURRICULUM DOC ###
with open("curriculum.txt") as f:
    curriculum = f.readlines()

curriculum = [line[:-1] for line in curriculum]

#get rid of \x characters
for i in range(len(curriculum)):
    test = curriculum[i].replace('\x93', "").replace('\x92', "").replace('\x94', "") \
        .replace('\x85', "")
    curriculum[i] = test

curriculum_full = ' '.join(curriculum)
curriculum_full = ''.join(ch for ch in curriculum_full if ch not in exclude)

filtered_words = [w.lower() for w in curriculum_full.split() if not w in stopwords.words('english')]
curriculum_dict = Counter(filtered_words)

#Take top 10
top_feats = [key for key in curriculum_dict if curriculum_dict[key] in sorted(curriculum_dict.values())[-10:]]
chosen_feats = ['growth', 'fixed', 'mindset', 'achieve', 'success', 'skill', 'effort', 'work', 'school']
###########################


#calculate score metric
df['score_vector'] = ""

for i in range(len(df['content'])):
    df['score_vector'][i] = []
    for kc in chosen_feats: 
        if kc in df['freq'][i].keys():
            df['score_vector'][i].append(1)
        else:
            df['score_vector'][i].append(0)

df['keyword_ratio'] = ""
for i in range(len(df['content'])):
    df['keyword_ratio'][i] = float(sum(df['score_vector'][i]))/len(df['score_vector'][i])

#Model Fit Script
from sklearn import svm
from sklearn import tree
from sklearn import linear_model
from sklearn.cross_validation import LeaveOneOut

#for i in range(25):
#    df['score_vector'][i].append(df['num_words'][i])
    
X = np.asarray([np.asarray(row, dtype='float64') for row in df['score_vector'][0:25]], dtype='float64')
# Just trying total number of words
X = np.zeros((25, 1))
for i in range(25):
    X[i,0] = df['num_words'][i]

#Trying num_words and keyword ratio as features
X = np.zeros((25, 2))
for i in range(25):
    X[i,0] = df['num_words'][i]
    X[i,1] = df['keyword_ratio'][i]

n = len(X)
y = np.asarray(df['score'][0:25], dtype='float64')

def our_round(x):
    num = round(x)
    if num > 5:
        num = 5
    elif num < 1:
        num = 1
    return num

#SVM Classifier
for kernel in ['rbf', 'linear', 'poly']:
    loo = LeaveOneOut(n)
    clf = svm.SVR(kernel=kernel)
    print "current kernel is " + kernel
    avediff = 0
    avediffSquared = 0
    for train, test in loo:
        clf.fit(X[train], y[train])
        prediction = our_round(clf.predict(X[test]))
        diff = abs(prediction - y[test])
        avediff += diff
        avediffSquared += diff**2
        print "Prediction: %.2f Answer: %.2f" % (prediction, y[test])
#    print "Average Difference: %.2f Standard Deviation: %.2f" % \
#            ((avediff / n), (avediffSquared / n))
    print
  
#Regression Tree Classifier  
loo = LeaveOneOut(n)
clf = tree.DecisionTreeRegressor()
avediff = 0
avediffSquared = 0
for train, test in loo:
    clf.fit(X[train], y[train])
    prediction = clf.predict(X[test])
    diff = abs(prediction - y[test])
    avediff += diff
    avediffSquared += diff**2
    print "Prediction: %.2f Answer: %.2f" % (prediction, y[test])
print "Average Difference: %.2f Standard Deviation: %.2f" % \
        ((avediff / n), (avediffSquared / n))
print

#Least Squares
loo = LeaveOneOut(n)
clf = linear_model.LinearRegression()
avediff = 0
avediffSquared = 0
for train, test in loo:
    clf.fit(X[train], y[train])
    prediction = our_round(clf.predict(X[test]))
    diff = abs(prediction - y[test])
    avediff += diff
    avediffSquared += diff**2
    print "Prediction: %.2f Answer: %.2f" % (prediction, y[test])
print "Average Difference: %.2f Standard Deviation: %.2f" % \
        ((avediff / n), (avediffSquared / n))
print

import cPickle as pickle
with open('afile', 'w') as f:
    pickle.dump(clf, f)