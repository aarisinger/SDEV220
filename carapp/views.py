from django.shortcuts import render
from .models import(Car)
from blog.models import(Post)
# Create your views here.

def cars(request):
    car = Car.objects.all()
    return render(request, 'car_list.html', {'car': car})

def index(request):
    sentence = "This is the first django view thing"
    greetings = "Hello"
    return render(request, 'index.html', {'sentence': sentence, "greetings": greetings})

def about(request):
    about = "This is the about page"
    return render(request, 'about.html', {'about': about})

def show_post(request):
    post = Post.objects.all()
    return render(request, 'post_list.html', {'post': post})


