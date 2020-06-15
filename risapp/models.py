from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Detail(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, \
             related_name='name')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name.username

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, \
             related_name='author')
    photo = models.ImageField(upload_to='media/', blank=True, null=True)
    caption = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    tag_name = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.caption
    
    
class Comments(models.Model):
    comment = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, \
             related_name='comenter')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, \
             related_name='posted_id')
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

class Likes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, \
           related_name='liked_post')
    user = models.ForeignKey(User, on_delete=models.CASCADE, \
           related_name='liker')


class Favorites(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, \
           related_name='favorite_post')
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE, \
           related_name='favorite_user')



class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, \
           related_name='follower')



class Tags(models.Model):
    tag_name = models.ManyToManyField(Post)

# class Photos(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, \
#            related_name='photos')
#     tag = models.ForeignKey(Post, on_delete=models.CASCADE, \
#            related_name='tag_photo')
