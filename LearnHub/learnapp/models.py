from django.db import models

from django.utils import timezone
# Create your models here.



class Video(models.Model):
    title = models.CharField(max_length=100)
    video=models.FileField(upload_to='video')
    info= models.CharField(max_length=1000)
    time=models.CharField(max_length=30)
    upload_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    


class chats(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    message=models.CharField(max_length=1000)
    time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
    
class Team(models.Model):  # Capital 'T' in class name and Model with capital M
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images')
    post= models.CharField(max_length=70)
    info = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class notes(models.Model):
    title=models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='pdfs/')  # 'pdfs/' is the folder inside MEDIA_ROOT where files are saved

    def _str_(self):
        return self.title


class exam(models.Model):

    title = models.CharField(max_length=200)
    pepar = models.URLField(max_length=500)

    def _str_(self):
        return self.title
    

# models.py
from django.db import models
from django.contrib.auth.models import User

class RegisteredUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        null=True,         # allow null temporarily
        blank=True,
        unique=True        # can keep unique True but null=True allows multiple nulls
    )
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    full_name = models.CharField(max_length=100, blank=True)  # Add this line

    bio = models.TextField()
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Question(models.Model):
    text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=1)  # 'A', 'B', 'C', or 'D'

    def __str__(self):
        return self.text

class UserScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    certificate_issued = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.score}"
    

class profileicon(models.Model):
    ph = models.ImageField(upload_to='images')










