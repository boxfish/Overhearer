from models import *
from django.contrib import admin

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('pId', 'username')
admin.site.register(Participant, ParticipantAdmin)

class DialogueAdmin(admin.ModelAdmin):
    list_display = ('dlgId', 'name', 'description', 'created_time', 'creator')
admin.site.register(Dialogue, DialogueAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('dialogue', 'content', 'created_time', 'author')
admin.site.register(Message, MessageAdmin)

class ResponderAdmin(admin.ModelAdmin):
    list_display = ('dialogue', 'respId', 'name', 'type')
admin.site.register(Responder, ResponderAdmin)

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('message', 'responder', 'created_time', 'explanation', 'preview')
admin.site.register(Response, ResponseAdmin)