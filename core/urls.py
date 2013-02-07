from django.conf.urls import patterns, url
from django.forms import FileField

urlpatterns = patterns('',
    url(r'^$', 'core.views.home'),
    url(r'^upload/$', 'core.views.upload'),
)
