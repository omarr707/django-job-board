from django.db import models

# Create your models here.

Jop_type = (
        ('Full Time','Full Time'),
        ('Part Time','Part Time'),
    )
    

class Jop(models.Model):
    title = models.CharField(max_length=30)
    #location
    Jop_type = models.CharField(max_length=30, choices=Jop_type)
    description = models.TextField(max_length=1000)
    publishedـat = models.DateField(auto_now=True)
    vacancv = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    
    

