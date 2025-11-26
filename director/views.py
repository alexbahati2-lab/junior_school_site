from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import HomePage, AboutPage, GalleryImage, Event
from .forms import HomePageForm, AboutPageForm, GalleryForm, EventForm
# director/views.py (add at the top with other imports)
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import ContactPage
from .forms import ContactPageForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def director_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'director/login.html')

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
@login_required
def edit_contact(request):
    contact, _ = ContactPage.objects.get_or_create(id=1)
    if request.method == 'POST':
        form = ContactPageForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ContactPageForm(instance=contact)
    return render(request, 'director/edit_contact.html', {'form': form})