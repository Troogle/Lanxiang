from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('ctb',
					   url(r'^$', 'views.home', name='home'),
					   url(r'^rules/$', 'views.rules', name='rules'),
					   url(r'^pool/$', 'views.pool', name='pool'),
					   url(r'^poolall/$', 'views.poolall', name='poolall'),
					   url(r'^pool/edit/$', 'views.beatmapedit', name='mapedit'),
					   url(r'^statistics/$', 'views.statistics', name='statistics'),
					   url(r'^statisticsfull/$', 'views.statisticsfull', name='statisticsfull'),
					   url(r'^match/$', 'views.matchlist', name='matchlist'),
					   url(r'^matchold/$', 'views.matchlistold', name='matchlistold'),
					   url(r'^match/add/$', 'views.matchlistadd', name='matchlistadd'),
					   url(r'^match/edit/(?P<match_id>\d+)/$', 'views.matchlistedit', name='matchlistedit'),
					   url(r'^match/edit/play/(?P<play_id>\d+)/', 'views.playedit', name='playedit'),
					   url(r'^staffs/$', 'views.staffs', name='staffs'),
					   url(r'^reward/$', 'views.reward', name='reward'),
					   url(r'^register/getcode$', 'views.checkcode'),
					   url(r'^admin/', include(admin.site.urls)),
)
