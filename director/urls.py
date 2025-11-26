# director/urls.py
from django.urls import path
from .views import dashboard, edit_home, edit_about, manage_gallery, manage_events, director_login, edit_contact
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', director_login, name='director_login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('edit-contact/', edit_contact, name='edit_contact'),  # <-- Make sure this is present
    path('edit-home/', edit_home, name='edit_home'),
    path('edit-about/', edit_about, name='edit_about'),
    path('gallery/', manage_gallery, name='manage_gallery'),
    path('events/', manage_events, name='manage_events'),
    # ... other patterns
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),


]
