from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

class Post(models.Model):
    image=models.ImageField(blank=False,null=False , default='default.jpg' ,upload_to='Blog')
    title=models.CharField(max_length=100)
    description=models.TextField()
    tag=TaggableManager()

class comment(models.Model):
    subject=models.CharField(max_length=100)
    description=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
