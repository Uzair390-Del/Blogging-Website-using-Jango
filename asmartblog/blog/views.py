from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})
  
#def home(request):
  #  return render(request,'home.html',{})
  
  

# Create your views here.
