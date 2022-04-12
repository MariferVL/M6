from django.shortcuts import render
from django.utils import timezone
from .models import Post


# Create your views here.

def home(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'bp/home.html', {'posts': posts})