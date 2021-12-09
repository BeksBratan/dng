from django.shortcuts import render 
from django.http import HttpResponse 
 
from blog.models import Post
 
 
def say_hello(request): 
    return HttpResponse('Hello Python!') 
 
 
def get_posts(request): 
    context = { 
        'posts': Post.objects.all() 
    } 
    return render(request, 'post_list.html', context)