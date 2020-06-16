from django.contrib import admin
from.models import Post,Comments,Likes,Favorites,Follow,Tags, ProfileDetail

# Register your models here.
admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Likes)
admin.site.register(Favorites)
admin.site.register(Follow)
admin.site.register(Tags)
admin.site.register(ProfileDetail)
