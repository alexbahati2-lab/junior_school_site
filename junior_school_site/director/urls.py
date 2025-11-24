from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('home/', views.edit_home, name='edit_home'),
    path('about/', views.edit_about, name='edit_about'),
    path('gallery/', views.manage_gallery, name='manage_gallery'),
    path('events/', views.manage_events, name='manage_events'),
]
