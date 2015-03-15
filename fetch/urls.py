from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^hello/$', 'fetch.views.hello', name='hello'),
    url(r'^dashboard/$', 'fetch.views.dashboard', name='dashboard'),
    url(r'^admin/', include(admin.site.urls)),
)
