from django import forms
from .models import HomePage, AboutPage, GalleryImage, Event

class HomePageForm(forms.ModelForm):
    class Meta:
        model = HomePage
        fields = ['welcome_text']

class AboutPageForm(forms.ModelForm):
    class Meta:
        model = AboutPage
        fields = ['mission', 'vision', 'history']

class GalleryForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['title', 'image', 'caption']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date', 'description']
