from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField(unique=True, null=True)
    location = models.CharField(max_length=30, default=None)
    about = models.TextField(max_length=250, default=None)
    # avatar = models.ImageField(null=True, default="static/images/avatar.svg")
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.email
    