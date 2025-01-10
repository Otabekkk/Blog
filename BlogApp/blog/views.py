from django.shortcuts import render
from .models import Post
def index(request):
    posts = Post.objects.all().order_by('-published_at')
    return render(request, 'blog/post_list.html', {'posts': posts})