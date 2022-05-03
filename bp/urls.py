from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name= 'home'),
    path('post',views.postIt, name='post-it'),
    path('post/<int:pk>/',views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('abp',views.abp, name='abp'),
    path('usersInfo', views.usersInfo, name='usersInfo'),
]

