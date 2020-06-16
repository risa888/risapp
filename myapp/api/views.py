from rest_framework import generics, mixins, viewsets
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import permissions                                        
from rest_framework.viewsets import ModelViewSet
from myapp.api.permissions import IsAdminUserOrReadOnly


from myapp.models import Post, Comments, Likes, Favorites, Follow, Tags, ProfileDetail
from myapp.api.serializers import (PostSerializer, CommentsSerializer, LikesSerializer,
                                    FavoritesSerializer, FollowSerializer, TagsSerializer,
                                    ProfileDetailSerializer)


class ProfileDetailViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = ProfileDetail.objects.all()
    serializer_class = ProfileDetailSerializer
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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]   

class CommentsListCreateAPIView(generics.ListCreateAPIView):

    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def comment_create(self, serializer):
        post_pk = self.kwargs.get("post_pk")
        post = get_object_or_404(Post, pk=post_pk)

        commenter = self.request.user

        post_queryset = Post.objects.filter(post=post,
                                                commenter=commenter)


        serializer.save(post=post, commenter=commenter)
    
# class TagsViewSet(mixins.ListModelMixin):

#     queryset = Tags.objects.all()
#     serializer_class = TagsSerializer

#     def tag_search(self):




