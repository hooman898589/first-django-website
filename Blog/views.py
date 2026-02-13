from django.contrib.admin.templatetags.admin_list import pagination
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.template.loader import get_template

from Blog.models import Post


def singlePoste(request, id):
    pass

def posts_view(request):

    # body=get_template("blog/blog.html")
    if request.GET.get('q')==None or request.GET.get('q')=='':
        if request.GET.get('tag')=="" or request.GET.get('tag')==None:

            posts = Post.objects.all().order_by('-id')
            pages=Paginator(posts,5)
            posts=pages.page(request.GET.get('page',1))

        else:
            posts = Post.objects.all().order_by('-id')
            posts=posts.filter(tag__name=request.GET.get('tag'))
            pages = Paginator(posts, 5)

            posts = pages.page(request.GET.get('page', 1))
    else:
        posts = Post.objects.all().order_by('-id')
        posts = posts.filter(title__icontains=request.GET.get('q'))
        pages = Paginator(posts, 5)
        posts = pages.page(request.GET.get('page', 1))


    return render(request, "blog/blog.html", {"posts": posts})