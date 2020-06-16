from django.urls import include, path
from rest_framework.routers import DefaultRouter
from myapp.api.views import (ProfileDetailViewSet, PostViewSet, CommentsViewSet,
                              CommentsListCreateAPIView)

router = DefaultRouter()
router.register(r"details", ProfileDetailViewSet)
router.register(r"posts", PostViewSet)
router.register(r"comments", CommentsViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("posts/<int:post_pk>/comments/", 
         CommentsListCreateAPIView.as_view())
    # path("risa/", PostCreateAPIView.as_view(),name="create-post")
    # path("risa/<int:pk>", PostDetailAPIView.as_view(),name="detail-post")

]