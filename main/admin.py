from django.contrib import admin

# Register your models here.
from .models import Image, Category

admin.site.register(Image)
admin.site.register(Category)
