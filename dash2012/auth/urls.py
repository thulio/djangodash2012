from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
import os

urlpatterns = patterns('auth.views',
    url(r'^login$', 'login', name='login-view'),
    url(r'^logout$', 'logout', name='logout-view'),
    # url(r'^dash2012/', include('dash2012.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)