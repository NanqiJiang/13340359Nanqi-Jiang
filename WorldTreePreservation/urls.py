"""WorldTreePreservation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('abount', views.abount, name='about'),
    path('program', views.program, name='program'),
    path('program/<int:id>', views.program_detail, name='program_detail'),
    path('gallery', views.gallery, name='gallery'),
    path('gallery-detail/<int:id>', views.gallery_detail, name='gallery-detail'),
    path('contact', views.contact, name='contact'),
    path('donate', views.donate, name='donate'),
    path('blog', views.blog, name='blog'),
    path('blog_del/<int:id>', views.blog_del, name='blog_del'),
    path('blog-single', views.blog_signle, name='blog_single')
]
