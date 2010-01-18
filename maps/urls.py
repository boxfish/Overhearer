from django.conf.urls.defaults import *

from maps.views import * 

urlpatterns = patterns('',
    url(r'^(?P<mapfile_path>.+)/static\.(?P<format>(jpeg|png))$', map_static, name='map_static'),
    url(r'^(?P<mapfile_path>.+)/tiles/(?P<zoom>[0-9]+)/(?P<x>[0-9]+)/(?P<y>[0-9]+)\.(?P<format>(jpeg|png))$', map_tiles, name='map_tiles'),
)

