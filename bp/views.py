from django.shortcuts import render, get_object_or_404, redirect
from  django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here. 

def home(request):
    return render(request, 'bp/home.html', {'home': home})

""" def search(request):
    return render(request, 'bp/search.html', {'search': search}) """

def postIt(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'bp/post-it.html', {'posts': posts})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'bp/post_detail.html', {'post': post})

@login_required
def post_new(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else: 
        form = PostForm()
    return render(request, 'bp/post_edit.html',{'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'bp/post_edit.html', {'form': form})

def usersInfo(request):
    users = User.objects.all()
    return render(request, 'bp/users_info.html', {'users': users})

def abp(request):
    return render(request, 'bp/abp.html', {'abp': abp})


