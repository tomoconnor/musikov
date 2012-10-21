from django.conf.urls import patterns, include, url
from musikovweb.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.defaults import *
from musikovweb.api import MidiChainResource


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
midichain_resource = MidiChainResource()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'musikovweb.views.home', name='home'),
    # url(r'^musikovweb/', include('musikovweb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^wibblescrote/', include(admin.site.urls)),
    (r'^$', index),
    (r'vote/(?P<dir>(up|down))/(?P<id>(\d+))',vote),
    (r'urlsubmit/',urlsubmit),
    (r'^api/', include(midichain_resource.urls)),

	
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
