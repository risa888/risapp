from django.urls import include, path
from rest_framework.routers import DefaultRouter
from risapp.api.views import (DetailViewSet, PostViewSet, CommentsViewSet)

router = DefaultRouter()
router.register(r"detail", DetailViewSet)
router.register(r"post", PostViewSet)
router.register(r"comment", CommentsViewSet)

urlpatterns = [
    path("", include(router.urls))
    # path("risa/", PostCreateAPIView.as_view(),name="create-post"),
    # path("risa/<int:pk>", PostDetailAPIView.as_view(),name="detail-post")

]