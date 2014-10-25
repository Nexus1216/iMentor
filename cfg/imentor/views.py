from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import pandas as pd
import numpy as np
#nltk.download()
from nltk.corpus import stopwords
import nltk, os, string
from collections import Counter
import cPickle as pickle
import string
from sklearn import linear_model
import re

def our_round(x):
    num = round(x)
    if num > 5:
        num = 5
    elif num < 1:
        num = 1
    return num

def clean_html(html):
    """
    Remove HTML markup from the given string.

    :param html: the HTML string to be cleaned
    :type html: str
    :rtype: str
    """

    # First we remove inline JavaScript/CSS:
    cleaned = re.sub(r"(?is)<(script|style).*?>.*?(</\1>)", "", html.strip())
    # Then we remove html comments. This has to be done before removing regular
    # tags since comments can contain '>' characters.
    cleaned = re.sub(r"(?s)<!--(.*?)-->[\n]?", "", cleaned)
    # Next we can remove the remaining tags:
    cleaned = re.sub(r"(?s)<.*?>", " ", cleaned)
    # Finally, we deal with whitespace
    cleaned = re.sub(r"&nbsp;", " ", cleaned)
    cleaned = re.sub(r"  ", " ", cleaned)
    cleaned = re.sub(r"  ", " ", cleaned)
    return cleaned.strip()

@csrf_exempt
def prep(request):
	#scr = {"score":"8"}
	#with open('afile','w') as f:
	#	pickle.dump(scr,f)
	return HttpResponse('testing')

@csrf_exempt
def score_message(request):
	print "entered post request"
	msg = request.POST['message_text']
	clf = pickle.load(open('afile', 'rb'))
	exclude = set(string.punctuation)
	msg_clean = clean_html(msg)
	print msg_clean
	no_stops = [w.lower() for w in msg_clean.split() if not w in stopwords.words('english')]
	no_punct = []
	for word in no_stops:
		no_punct.append(''.join([ch for ch in word if ch not in exclude]))
	no_stops = ' '.join(no_punct)
	num_words = len(no_stops.split())
	
	result = our_round(clf.predict(np.asarray([num_words])))
	
	json_data = json.dumps({"data":result})
	print json_data
	return HttpResponse(json_data)
