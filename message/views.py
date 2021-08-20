
from django.shortcuts import render, redirect, get_object_or_404
from .models import Message
from .forms import *
from django.utils import timezone
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
# Create your views here.
def detailMessage(request, messageId): 
    message = get_object_or_404(Message, pk = messageId) 
    replys = Reply.objects.filter(messageId=messageId,replyId__isnull=True).order_by('-id')
    replyForm = ReplyForm()
    return render(request, 'detailMessage.html', {'message':message,'replys':replys,'replyForm':replyForm})

def messageBox(request):#메세지함
    userinfo =get_user_model().objects.all()
    messages=Message.objects.filter( to = request.user).order_by('-id')|Message.objects.filter(   writer = request.user).order_by('-id')
    paginator = Paginator(messages, 10)
    page = request.GET.get('page')
    message = paginator.get_page(page)
    replys = Reply.objects.all().order_by('-id')
    #paginatorPost = Paginator(replys,1)
    #page = request.GET.get('page')
    #reply = paginatorPost.get_page(page)
    return render(request,"messageBox.html",{'message':message,'replys':replys,'userinfo':userinfo})


def newMessage(request,to):
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.to = to
            message.writer = request.user
            message.pub_date = timezone.now() 
            message.save()
            return redirect("detailMessage",message.id)
    else:
        form = MessageForm()
        print(to)
        return render(request, 'newMessage.html', {'form':form,'to':to})
def replyMessage(request, messageId):
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.messageId = Message.objects.get(pk = messageId)
            reply.writer = request.user
            reply.pub_date = timezone.now()
            reply.save()
    return redirect('/message/detailMessage/'+str(messageId))

def deleteMessage(request,messageId):
   deletePost = get_object_or_404(Message,pk=messageId)
   
   deletePost.delete() #삭제해주는 메소드
   return redirect('messageBox')

def deleteReply(request,replyId,messageId):
   deleteReply = get_object_or_404(Reply,pk=replyId)
   
   deleteReply.delete() #삭제해주는 메소드
   return redirect('detailMessage',messageId)