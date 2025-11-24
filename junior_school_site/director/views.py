from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import HomePage, AboutPage, GalleryImage, Event
from .forms import HomePageForm, AboutPageForm, GalleryForm, EventForm

@login_required
def dashboard(request):
    return render(request, 'director/dashboard.html')

@login_required
def edit_home(request):
    home, _ = HomePage.objects.get_or_create(id=1)
    if request.method == 'POST':
        form = HomePageForm(request.POST, instance=home)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = HomePageForm(instance=home)
    return render(request, 'director/edit_home.html', {'form': form})

@login_required
def edit_about(request):
    about, _ = AboutPage.objects.get_or_create(id=1)
    if request.method == 'POST':
        form = AboutPageForm(request.POST, instance=about)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AboutPageForm(instance=about)
    return render(request, 'director/edit_about.html', {'form': form})

@login_required
def manage_gallery(request):
    images = GalleryImage.objects.all()
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage_gallery')
    else:
        form = GalleryForm()
    return render(request, 'director/manage_gallery.html', {'form': form, 'images': images})

@login_required
def manage_events(request):
    events = Event.objects.all()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_events')
    else:
        form = EventForm()
    return render(request, 'director/manage_events.html', {'form': form, 'events': events})
