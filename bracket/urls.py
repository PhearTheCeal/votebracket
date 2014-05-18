
from django.conf.urls import patterns, url

from bracket import views

urlpatterns = patterns('',
        url(r'^$', views.index, name="index"),
        url(r'^(?P<tournament_id>\d+)/$', views.tournament, name="tournament")
)
