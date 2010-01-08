from django.conf.urls.defaults import *

from maps.views import * 

urlpatterns = patterns('',
    url(r'^test$', test, name='test'),
)

