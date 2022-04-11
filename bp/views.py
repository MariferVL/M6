from django.shortcuts import render

# Create your views here.

def home_list(request):
    return render(request, 'bp/home_list.html', {})