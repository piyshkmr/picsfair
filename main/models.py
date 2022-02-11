from django.db import models
import uuid


# Create your models here.


class Category(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Image(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=300)
    description = models.TextField()
    url = models.ImageField(upload_to='images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
