from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

# Create your models here.


# Default User model
class User(AbstractUser):
    pass


# User profile model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


# Agent model
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.email


# Lead model
class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField(unique=True, null=True)
    location = models.CharField(max_length=30, default=None)
    about = models.TextField(max_length=250, default=None)
    # avatar = models.ImageField(null=True, default="static/images/avatar.svg")
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



def post_user_create_signal(sender, instance, created, **kwargs):
    print(instance, created)
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_create_signal, sender=User)