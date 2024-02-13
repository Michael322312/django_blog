from django.shortcuts import render
from blog.models import Post
# Create your views here.

def posts_list(request):
    posts = Post.objects.all()
    context = {
        "posts_list": posts
    }
    return render(
        template_name="blog/posts_list.html",
        context=context,
        request=request
    )