from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.core.mail import EmailMessage
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import urllib.parse


# def mail(request):
#     if request.method =='POST':
#         name= request.POST.get('name')
#         email= request.POST.get('email')
#         subject= request.POST.get('subject')
#         body= request.POST.get('body')

#         data={
#             'name':name,
#             'email':email,
#             'subject':subject,
#             'body':body,
#         }
#         #print(data)
#         body= '''
#         New Mail :{}
#         From : {}'''.format(data['body'],data['email'])
#         send_mail(data['subject'],body,'',['eunmoong@gmail.com'])
#     return render(request,'mail.html')

# def sendmail(request):
#     send_mail('Hello Dear',
#               'Hi there, lalaala',
#               'gpg5005@naver.com',
#               ['eunmoong@gmail.com'],
#               fail_silently=False)

#     return redirect('/')


def mail(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST, request.FILES)
        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.save()
            subject = contact.name
            message = contact.message
            email = contact.email
            mail = EmailMessage(subject, message, to=[email])
            mail.send()
            return redirect('index')
    else:
        contact_form = ContactForm()
        return render(request, 'mail.html', {'contact_form':contact_form})