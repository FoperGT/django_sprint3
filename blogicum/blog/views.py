from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.all().order_by('-pub_date')

    return render(request, "blog/index.html", {"posts": posts})


def post_detail(request, pk):
    post = Post.objects.get(id=pk)

    return render(request, "blog/detail.html", {"post": post})


def category_posts(request, category_slug):
    posts = Post.objects.filter(category=category_slug)

    return render(
        request,
        "blog/category.html",
        {"category_slug": category_slug,
         "posts": posts}
    )
