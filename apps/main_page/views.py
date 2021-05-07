from django.shortcuts import render

from apps.posts.models import Post


def index(request):
    posts = Post.objects.all()  #SELECT * FROM post;
    return render(request=request, template_name='pages/index.html', context={'posts': posts})
