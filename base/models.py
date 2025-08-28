from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICE = [
        ('super_admin', "Super Admin"),
        ('account', "account"),
    ]
    profile_image = models.ImageField(upload_to="profile/image", blank=True, null=True)
    role = models.CharField(max_length=100, choices=ROLE_CHOICE, default='account')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Channel(models.Model):
    name = models.CharField(max_length=250)
    bio = models.TextField(blank=True, null=True)
    owner = models.OneToOneField(CustomUser, related_name="owner", on_delete=models.CASCADE)
    banner = models.ImageField(upload_to='banner', null=True, blank=True)
    profile_icon = models.ImageField(upload_to='profile', null=True, blank=True)
    subscribe = models.ManyToManyField(CustomUser, related_name='subscribe', null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

class Video(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    owner = models.ForeignKey(CustomUser, related_name='videoowner', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    video = models.FileField(upload_to='video/video')
    thumbnail_image = models.ImageField(upload_to='video/image', null=True, blank=True)
    views = models.ManyToManyField(CustomUser, related_name='Views', null=True, blank=True)
    like = models.ManyToManyField(CustomUser, related_name='Like', null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

class Playlist(models.Model):
    name = models.CharField(max_length=250)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class PersonSaved(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)


