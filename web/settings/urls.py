from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('ctb',
url(r'^$', 'views.home',name='home'),
url(r'^rules/$', 'views.rules',name='rules'),
url(r'^pool/$', 'views.pool',name='pool'),
url(r'^statistics/$', 'views.statistics',name='statistics'),
url(r'^staffs/$', 'views.staffs',name='staffs'),
url(r'^support/$', 'views.support',name='support'),
url(r'^register/$', 'views.register',name='register'),
    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^web/', include('web.foo.urls')),
)
