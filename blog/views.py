from django.shortcuts import render, get_object_or_404
from .models import Post, AboutMe, Category
import markdown
# Create your views here.

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={
        'post_list': post_list
    })

def category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=category).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    post.body = markdown.markdown(post.body, extensions = [
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])

    post.increase_views() # 阅读量 + 1

    return render(request, 'blog/detail.html', context={'post': post})

def about(request):
    aboutme = get_object_or_404(AboutMe)
    aboutme.body = markdown.markdown(aboutme.body, extensions = [
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])

    return render(request, 'blog/about.html', context={'about': aboutme})