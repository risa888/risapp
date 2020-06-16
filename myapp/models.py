from django.db import models
from django.contrib.auth.models import User

class ProfileDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    introduction = models.TextField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media/', blank=True, null=True)
    caption = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    tag_name = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return str(self.author)
    
    
class Comments(models.Model):
    comment = models.CharField(max_length=500)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

class Likes(models.Model):
    liked_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    liker = models.ForeignKey(User, on_delete=models.CASCADE)


class Favorites(models.Model):
    favorite_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    favorite = models.ForeignKey(User, default=None, on_delete=models.CASCADE)



class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE)



class Tags(models.Model):
    tag_name = models.ManyToManyField(Post)


