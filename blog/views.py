from django.shortcuts import render

from .models import Post

def detail(request, slug):
    post = Post.objects.get(slug=slug)

    return render(request, "blog/detail.html", {
        'post': post
    })
