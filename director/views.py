from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Import models from main app
from main.models import HomePage, AboutPage, Gallery, Event, ContactPage
# Import forms from director app
from director.forms import HomePageForm, AboutPageForm, GalleryForm, EventForm, ContactPageForm

# --- Director login ---
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


# --- Dashboard ---
@login_required
def dashboard(request):
    return render(request, 'director/dashboard.html')


# --- Edit Home Page ---
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


# --- Edit About Page ---
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


# --- Manage Gallery ---
@login_required
def manage_gallery(request):
    images = Gallery.objects.all()
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage_gallery')
    else:
        form = GalleryForm()
    return render(request, 'director/manage_gallery.html', {'form': form, 'images': images})


# --- Manage Events ---
@login_required
def manage_events(request):
    events = Event.objects.all().order_by('-date')
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_events')
    else:
        form = EventForm()
    return render(request, 'director/manage_events.html', {'form': form, 'events': events})


# --- Edit Contact Page ---
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
