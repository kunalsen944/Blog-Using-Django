from django import forms
from django.contrib.auth.models import User
from blog_app.models import Post
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        exclude=['author','date']

class UpdatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category','title','text','image']
