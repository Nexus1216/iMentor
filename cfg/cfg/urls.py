from django.conf.urls import patterns, include, url
from django.contrib import admin
from cfg import views
from imentor import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cfg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^imentor/', include('imentor.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
