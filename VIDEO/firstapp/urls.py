
from django.urls import path
from .views import Home,about,contact,upload

urlpatterns = [
    path('Home',Home,name="Home"),
    path('about',about,name="about"),
    path('contact',contact,name="contact"),
    path('upload/',upload,name="upload"),
    
    
]

