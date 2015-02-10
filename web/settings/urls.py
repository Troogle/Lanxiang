from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('ctb',
url(r'^$', 'views.home',name='home'),
url(r'/rules^$', 'views.rules',name='rules'),
url(r'/pool^$', 'views.pool',name='pool'),
url(r'/pool^$', 'views.statistics',name='statistics'),
url(r'/pool^$', 'views.staffs',name='staffs'),
url(r'/pool^$', 'views.support',name='support'),
url(r'/pool^$', 'views.register',name='register'),
    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^web/', include('web.foo.urls')),
)
