from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.utils import timezone
from .forms import  *
from user.models import  *
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.db.models.fields import json
import simplejson as json

# Create your views here.
def index(request):
    post_list = Post.objects.all().order_by('-id')
    paginatorPost = Paginator(post_list,5)
    page = request.GET.get('page')
    Posts = paginatorPost.get_page(page)
    return render(request,"index.html",{'postList':Posts})

def userPage(request,goTo):
    posts=Post.objects.filter( writer = goTo).order_by('-id')
    userinfo =get_user_model().objects.all()
    print(userinfo)
    print(posts)
    return render(request,"userPage.html",{ 'posts': posts,'goTo':goTo,'userinfo':userinfo})

#새로운 글 작성
def new(request):
    if request.method == 'POST': #글 작성 후 저장버튼 눌렀을 때
        post_form = PostForm(request.POST,request.FILES)
        if post_form.is_valid():# 이 form을 유효한지 검사후 유효하면 save해줌 (임시저장)
            post = post_form.save(commit = False)#임시저장 해주는 이유는 model에 있는 필드 중 new date를 안 담았음 (commit=False)
            post.writer = request.user
            post.pub_date = timezone.now() 
            post.save()
            return redirect("index")
    else:
        post_form = PostForm()
        context = {}
        context['postsform'] = post_form
        return render(request,'new.html',context)
    #댓글작성





#게시글 삭제
def delete(request,postId):
   deletePost = get_object_or_404( Post,pk=postId)
   deletePost.delete() #삭제해주는 메소드
   return redirect('index')


def post_likes(request):
    if request.is_ajax():
        blog_id = request.GET['blog_id']
        post = Post.objects.get(id=blog_id)
        user= request.user
        
        if post.like.filter(id=user.id).exists():
            post.like.remove(user)
            message = "좋아요 취소"
        else:
            post.like.add(user)
            message="좋아요"

    context = {
        'like_count': post.like.count(),
        'message': message
    }
    return HttpResponse(json.dumps(context), content_type='application/json')

