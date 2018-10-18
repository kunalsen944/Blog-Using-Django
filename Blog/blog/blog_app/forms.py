from django import forms
from django.contrib.auth.models import User
from blog_app.models import Post,Comment
from pagedown.widgets import PagedownWidget



class AddPost(forms.ModelForm):
    text=forms.CharField(widget=PagedownWidget)

    class Meta:
        model = Post
        exclude=['author','date']

class UpdatePost(forms.ModelForm):
    text=forms.CharField(widget=PagedownWidget)

    class Meta:
        model = Post
        fields = ['category','title','text','image']
