from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
def posts(request):
    posts = Post.objects.all()
    return render(request,"posts.html",{"posts":posts})