from django.http import Http404
from django.shortcuts import render
from .models import Post

def index(request):
    return render(request, 'blog/base.html', {})

def post_detail(request, id):
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404("No Post found.")
    return render(request, 'blog/post/detail.html', {
        'post': post
    })

def post_list(request):
    posts = Post.published.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/post/list.html', context=context)