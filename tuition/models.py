from django.db import models
from django.contrib.auth.models import User

class TuitionPost(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    class_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    salary = models.IntegerField()
    days_per_week = models.IntegerField()
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title