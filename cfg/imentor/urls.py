from django.conf.urls import patterns, url
from imentor import *

urlpatterns = patterns('',
	url(r'^score_message/$', views.score_message, name='score_message'),
	url(r'^prep/$', views.prep, name='prep'),
	)
