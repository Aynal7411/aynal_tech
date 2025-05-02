from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(blank=True)
    technologies = models.CharField(max_length=200)
    date_created = models.DateField(auto_now_add=True)

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField()
    category = models.CharField(max_length=100)

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)