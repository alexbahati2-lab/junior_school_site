from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Teacher, News, Gallery

def home(request):
    news = News.objects.all().order_by('-date_posted')[:3]
    gallery = Gallery.objects.all()[:6]
    return render(request, 'home.html', {'news': news, 'gallery': gallery})

def about(request):
    teachers = Teacher.objects.all()
    return render(request, 'about.html', {'teachers': teachers})

def contact(request):
    return render(request, 'contact.html')

def events(request):
    return render(request, 'events.html')
 
