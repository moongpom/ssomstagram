from django import forms
from .models import *

# Create your models here.
class PostForm(forms.ModelForm):
    title = forms.CharField(label='제목', max_length=500, 
        widget=forms.Textarea(attrs={'rows':'1', 'cols': '80'}))
    body = forms.CharField(label='내용', max_length=1000, 
        widget=forms.Textarea(attrs={'rows':'15', 'cols': '80'}))
    class Meta:
        model = Post
        fields =['title','body','image']




class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')