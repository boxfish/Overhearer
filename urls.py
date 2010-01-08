import os
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from views import *
#from dialogues.views import *

urlpatterns = patterns('',
    (r'^$', indexHandler),
    (r'^dialogues/', include('dialogues.urls')),
    (r'^maps/', include('maps.urls')),
    (r'^admin/(.*)', admin.site.root),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(.*)', 'django.views.static.serve', {'document_root': os.path.join("./", 'static')}),
)
