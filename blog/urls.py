from django.urls import path

import blog.views as blog_views

urlpatterns = [
    path("", blog_views.posts_list, name="posts_list")
]