from rest_framework import serializers
from risapp.models import Post, Comments, Likes, Favorites, Follow, Tags, Detail

class DetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Detail
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"

class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = "__all__"
        

class LikesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Likes
        fields = "__all__"

class FavoritesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorites
        fields = "__all__"

class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follow
        fields = "__all__"

class TagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tags
        fields = "__all__"
