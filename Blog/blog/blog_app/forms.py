from django import forms
from django.contrib.auth.models import User
from blog_app.models import Post
from django.contrib.auth.forms import UserCreationForm
from pagedown.widgets import PagedownWidget


class SignupForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


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
