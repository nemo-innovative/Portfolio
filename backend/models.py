from django.db import models

# Create your models here.
class BannerLoader(models.Model):
    title = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img/', null=True, blank=False)
    category = models.CharField(max_length=50)
    action = models.CharField(max_length=255)
    status = models.BooleanField()

    def __str__(self):
        return self.title
    
class Service (models.Model):
    image = models.ImageField(upload_to='img/', null=True, blank=False)
    title = models.CharField(max_length=255)
    desc = models.TextField()
    
    def __str__(self):
        return self.title
    
class Clients(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img/', null=True, blank=False)
    action = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

class Testemonial(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img/', null=True, blank=False)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Team(models.Model):
    name = models.CharField(max_length=255)
    post = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img/', null=True, blank=False)
    fb = models.CharField(max_length=255)
    ig = models.CharField(max_length=255)
    x = models.CharField(max_length=255)
    In = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class About(models.Model):
    about = models.TextField()
    mission = models.TextField()
    vision = models.TextField()
    approach = models.TextField()
    
class Contact(models.Model):
    desc = models.TextField()
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    map = models.CharField(max_length=255)