from django.urls import path

from social.api.views import post_list, post_detail, update_post, delete_post, create_post

urlpatterns = [
    path('posts/', post_list),
    path('posts/<int:pk>', post_detail),
    path('posts/<int:pk>/update', update_post),
    path('posts/<int:pk>/delete', delete_post),
    path('posts/new/', create_post),
]