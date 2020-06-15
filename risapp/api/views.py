from rest_framework import generics, mixins, viewsets
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet


from risapp.models import Post, Comments, Likes, Favorites, Follow, Tags, Detail
from risapp.api.serializers import (PostSerializer, CommentsSerializer, LikesSerializer,
                                    FavoritesSerializer, FollowSerializer, TagsSerializer,
                                    DetailSerializer)


class DetailViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class PostViewSet(ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def comment_create(self):
        
        author = self.request.user

       
    

class CommentsViewSet(ModelViewSet):

    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated]

    
# class TagsViewSet(mixins.ListModelMixin):

#     queryset = Tags.objects.all()
#     serializer_class = TagsSerializer

#     def tag_search(self):


