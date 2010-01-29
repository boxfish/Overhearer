from django.conf.urls.defaults import *

from dialogues.views import *

urlpatterns = patterns('',
    url(r'^test/$', testHandler),
    url(r'^(?P<dlgId>.+)/messages/(?P<msgId>.+)/$', messageHandler),
    url(r'^(?P<dlgId>.+)/messages/$', messagesHandler),
    url(r'^(?P<dlgId>.+)/participants/(?P<pId>.+)/$', participantHandler),
    url(r'^(?P<dlgId>.+)/participants/$', participantsHandler),
    url(r'^(?P<dlgId>.+)/responses/(?P<respId>.+)/$', responseHandler),
    url(r'^(?P<dlgId>.+)/responses/$', responsesHandler),
    url(r'^(?P<dlgId>.+)/plangraph/$', plangraphHandler),
    url(r'^(?P<dlgId>.+)/$', dialogueHandler),
    url(r'^$', dialoguesHandler),
)
