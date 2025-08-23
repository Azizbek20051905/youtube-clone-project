from django.shortcuts import render
from django.views import generic
from .models import CustomUser, Video, Channel, PersonSaved, Playlist, Comment

# Create your views here.
class HomePage(generic.ListView):
    model = Video
    template_name = "index.html"
    