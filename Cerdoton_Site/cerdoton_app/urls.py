from django.conf.urls import patterns, url

from cerdoton_app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pig_id>\d+)/$', views.generalData, name='generalData'),
    url(r'^(?P<pig_id>\d+)/status/$', views.status, name='status'),
    url(r'^graphData/$', views.graphData, name='graphData'),
)
