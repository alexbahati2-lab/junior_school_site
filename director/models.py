

# Create your models here.
from django.db import models

class HomePage(models.Model):
    welcome_text = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Home Page Content"


class AboutPage(models.Model):
    mission = models.TextField()
    vision = models.TextField()
    history = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "About Page Content"


class GalleryImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} ({self.date})"
# director/models.py or main/models.py
from django.db import models

class ContactPage(models.Model):
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return "Contact Info"
