from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


# Create your views here.

def home(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'bp/home.html', {'posts': posts})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'bp/post_detail.html', {'post': post})
