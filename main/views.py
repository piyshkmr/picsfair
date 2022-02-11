from main.models import Category, Image
from django.shortcuts import render

# Create your views here.


def index(request):
    images = Image.objects.all()
    categories = Category.objects.all()
    return render(request, "main/index.html", {"images": images, "categories": categories})


def category(request, id):
    images = Image.objects.filter(category=id)
    categories = Category.objects.all()
    category = Category.objects.get(id=id)
    return render(request, "main/index.html", {"images": images, "categories": categories, "currentCategory": category})


def search(request):
    query = request.GET.get("query")
    images = Image.objects.filter(
        title__icontains=query, description__icontains=query)
    return render(request, "main/search.html", {"images": images, "query": query})
