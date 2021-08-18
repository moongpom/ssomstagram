from django.urls import path
from .views import *

urlpatterns = [
   #게시글
   path('newPost/',new,name="newPost"),
   path('deletePost/<str:postId>',delete,name="deletePost"),
   path('userPage/<str:goTo>',userPage,name="userPage"),
   path('like/', post_likes, name="post_likes"),
]