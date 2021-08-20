
from django.urls import path
from .views import *

urlpatterns = [
   path('newMessage/<str:to>',newMessage,name='newMessage'),
   path('replyMessage/<str:messageId>',replyMessage,name='replyMessage'),
   path('messageBox/',messageBox,name='messageBox'),
   path('detailMessage/<str:messageId>',detailMessage,name='detailMessage'),
   path('deleteMessage/<str:messageId>',deleteMessage,name='deleteMessage'),
   path('deleteReply/<str:replyId>/<str:messageId>',deleteReply,name='deleteReply'),
]
