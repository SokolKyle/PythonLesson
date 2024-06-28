from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=500, blank=True)
    username = models.CharField(max_length=200, blank=True)
    short_info = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to="profiles/", default="profiles/user-default.png")
    social_github = models.CharField(max_length=200, blank=True)
    social_youtube = models.CharField(max_length=200, blank=True)
    social_website = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


def profile_updated(sender, instance, created, **kwargs):
    print("Profile Saved!")
    print("sender:", sender)
    print("instance:", instance)
    print("created:", created)


post_save.connect(profile_updated, sender=Profile)
