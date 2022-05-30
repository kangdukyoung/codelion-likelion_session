from django.shortcuts import render, redirect
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    posts = Blog.objects.all().order_by('-pub_date')
    paginator = Paginator(posts,4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    return render(request,'home.html',{'posts':posts})


def new(request):
    if request.method == "POST":
        blog = Blog()
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('/')
    else:
        return render(request,'new.html')


def detail(request, blog_id):
    blog = Blog.objects.get(id = blog_id)
    return render(request,'detail.html',{'blog':blog})

def delete(request, blog_id):
    Blog.objects.get(id = blog_id).delete()
    return redirect('/')

def update(request, blog_id):
    if request.method == 'POST':
        blog = Blog.objects.get(id = blog_id)
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('/blog/'+str(blog_id))
    else:
        blog = Blog.objects.get(id = blog_id)
        return render(request, 'update.html',{'blog':blog})

