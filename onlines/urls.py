from django.urls import path
from .views import   menu_detail,menu_list,product_list,product_detail 

urlpatterns = [
    path("products/", product_list, name="product-list"),
    path("products/<int:pk>/", product_detail, name="product-detail"),
    path("menu/",  menu_list, name=" menu-list"),
    path("menu/<int:pk>/", menu_detail, name="menu-detail"),

]