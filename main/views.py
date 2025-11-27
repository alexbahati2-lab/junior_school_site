from django.shortcuts import render
from .models import Teacher, News, Gallery, Event

def home(request):
    news = News.objects.all().order_by('-date_posted')[:3]
    gallery = Gallery.objects.all()[:6]
    events = Event.objects.all().order_by('-date_posted')[:3]
    
    return render(request, 'home.html', {
        'news': news,
        'gallery': gallery,
        'events': events
    })

def about(request):
    teachers = Teacher.objects.all()
    return render(request, 'about.html', {'teachers': teachers})

def contact(request):
    return render(request, 'contact.html')

def events(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'events.html', {'events': events})

def gallery(request):
    images = Gallery.objects.all()
    return render(request, 'gallery.html', {'images': images})
