
from django.urls import path
from .views import *

urlpatterns = [
   path('newMessage/<str:to>/<str:title>',newMessage,name='newMessage'),
   path('replyMessage/<str:messageId>',replyMessage,name='replyMessage'),
   path('messageBox/',messageBox,name='messageBox'),
   path('detailMessage/<str:messageId>',detailMessage,name='detailMessage'),
   path('deleteMessage/<str:messageId>',deleteMessage,name='deleteMessage'),
]
