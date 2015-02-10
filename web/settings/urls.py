from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('ctb',
					   url(r'^$', 'views.home', name='home'),
					   url(r'^rules/$', 'views.rules', name='rules'),
					   url(r'^pool/$', 'views.pool', name='pool'),
					   url(r'^statistics/$', 'views.statistics', name='statistics'),
					   url(r'^staffs/$', 'views.staffs', name='staffs'),
					   url(r'^support/$', 'views.support', name='support'),
					   url(r'^register/$', 'views.register', name='register'),
					   url(r'^register/getcode$', 'views.checkcode'),
					   url(r'^admin/', include(admin.site.urls)),
)
