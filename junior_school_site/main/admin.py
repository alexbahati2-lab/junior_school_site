from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Teacher, News, Gallery

admin.site.register(Teacher)
admin.site.register(News)
admin.site.register(Gallery)
