from django.db import models
import datetime  # needed for default dates

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='teachers/', blank=True)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    caption = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.title or self.caption


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    # Set a default to fix the non-nullable field problem
    date = models.DateField(default=datetime.date.today)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.date})"


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


class ContactPage(models.Model):
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return "Contact Info"
