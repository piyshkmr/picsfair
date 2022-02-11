from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("category/<str:id>/", views.category, name="category"),
    path("search", views.search, name="search"),
]
