from django.db import models
from tutors.models import TutorProfile
from tuition.models import TuitionPost

class Application(models.Model):

    tutor = models.ForeignKey(TutorProfile, on_delete=models.CASCADE)
    tuition = models.ForeignKey(TuitionPost, on_delete=models.CASCADE)

    message = models.TextField()

    def __str__(self):
        return self.tuition.title