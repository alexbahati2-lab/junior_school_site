from django import forms
from .models import HomePage, AboutPage, GalleryImage, Event, ContactPage

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

class ContactPageForm(forms.ModelForm):
    class Meta:
        model = ContactPage
        fields = ['phone', 'email', 'address']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }        
