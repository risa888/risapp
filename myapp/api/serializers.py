from rest_framework import serializers
from myapp.models import Post, Comments, Likes, Favorites, Follow, Tags, ProfileDetail

class ProfileDetailSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProfileDetail
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    # post_id = CommentsSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = "__all__"

class CommentsSerializer(serializers.ModelSerializer):
    
    # commenter = serializers.StringRelatedField(read_only=True)
    post_id = PostSerializer(many=True, read_only=True)

    
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
