from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class TutorProfile(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    phone_number=models.IntegerField()
    father_number = models.IntegerField()
    NID= models.IntegerField()

    experience = models.TextField()
    preferred_area = models.CharField(max_length=100)
    
    def __str__(self):
        return self.full_name