from django.conf.urls import patterns, url

from cerdoton_app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pig_id>\d+)/$', views.generalData, name='generalData'),
    url(r'^(?P<pig_id>\d+)/status/$', views.status, name='status'),
    url(r'^score/$', views.score, name='score'),
    url(r'^graphData/weight/$', views.graphDataWeight, name='graphDataWeight'),
    url(r'^graphData/fat/$', views.graphDataFat, name='graphDataFat'),
    url(r'^graphData/muscle/$', views.graphDataMuscle, name='graphDataMuscle'),
)
