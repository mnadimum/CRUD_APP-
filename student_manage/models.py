from django.db import models

# Create your models here.

CHOICES = [
    ('ME', 'ME'),
    ('CSE', 'CSE'),
    ('ECE', 'ECE'),
    ('AI', 'AI'),
    ('ML', 'ML'),
]
class Student(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    branch = models.CharField(max_length=20, choices=CHOICES)
    
    def __str__(self):
        return self.fname
    
    
