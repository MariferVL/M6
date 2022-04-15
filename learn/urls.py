"""learn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/password_reset/', views.PasswordResetView.as_view(template_name="registration/password_reset.html"),
        name="password_reset"),
    path('accounts/password_reset/done/',views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"),
        name="password_reset_done"),
    path('accounts/already_logged_in/',views.PasswordResetDoneView.as_view(template_name="registration/already_logged_in.html"),
        name="already_logged_in"),
    path('', include('bp.urls')),
    path("accounts/", include("accounts.urls")),
]
