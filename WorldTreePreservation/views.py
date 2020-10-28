#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author:Ruan Time:2020/10/25 17:29
from django.shortcuts import render, HttpResponse, redirect, reverse
from comment.models import Comment

def home(request):
    return render(request, 'index.html')


def abount(request):
    return render(request, 'about.html')


def program(request):
    return render(request, 'program.html')


def program_detail(request, id):
    return render(request, 'program-detail.html', context={'id': id})


def gallery(request):
    return render(request, 'gallery.html')


def gallery_detail(request, id):
    return render(request, 'gallery-detail.html', context={'id': id})


def contact(request):
    return render(request, 'contact.html')


def blog(request):
    all = Comment.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        comment = request.POST.get('comment')
        print(username)
        print(comment)
        comm = Comment(username=username, comment=comment)
        comm.save()

    return render(request, 'blog.html', context={'all': all})


def blog_del(request, id):
    c = Comment.objects.get(id=id)
    c.delete()
    return redirect(reverse('blog'))


def blog_signle(request):
    return render(request, 'blog-single.html')


def donate(request):
    return render(request, 'donate.html')




