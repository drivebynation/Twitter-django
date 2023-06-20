from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.get_posts()
    context = {'posts': posts}
    return render(request, 'post_list.html', context)

# Create your views here.
