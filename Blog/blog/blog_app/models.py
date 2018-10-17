from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image




class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    category=models.CharField(max_length=50,default='blog')
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=20000)
    image=models.ImageField(upload_to='post_image',default='blog.png')
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comment',on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    email=models.EmailField()
    text = models.TextField(default='Nice Post')
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
