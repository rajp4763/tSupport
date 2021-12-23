from django.shortcuts import render
from django.http import HttpResponse
from blog.models import *
# Create your views here.
def index(request):
    try:
        slides = Slider.objects.all()[:5]
        context = {'slides':slides}
    except:
        context = {}
    return render(request,'index.html',context)


def blogs(request):
    posts = Post.objects.all()[:11]
    cat = Category.objects.all()[:5]
    context = {'posts':posts,'cat':cat}
    return render(request,'blog/blogs.html',context)

def blog(request,url):
    try:
        post = Post.objects.get(url = url)
    except:
        post = Post.objects.filter(url = url)
    cat = Category.objects.all()[:5]
    context = {'post':post,'cat':cat}
    return render(request, 'blog/blog.html',context)
