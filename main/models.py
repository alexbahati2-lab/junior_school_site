from django.db import models

# Create your models here.
from django.db import models

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
    caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.caption
