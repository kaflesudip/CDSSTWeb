from django.conf import settings
from django.conf.urls import patterns, include, url
from TelecomApp.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'TelecomApp.views.home'),
    url(r'^overview/?$', 'TelecomApp.views.overview'),
    url(r'^output/?$', 'TelecomApp.views.output'),
    url(r'^tools/?$', 'TelecomApp.views.tools'),
    url(r'^team/?$', 'TelecomApp.views.team'),
    # url(r'^TelecomDA/', include('TelecomDA.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('django.views.static',
	(r'^%s(?P<path>.*)' % settings.MEDIA_URL, 'serve', {'document_root': settings.MEDIA_ROOT})
)
