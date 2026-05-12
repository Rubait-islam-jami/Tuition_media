from django import forms
from .models import TutorProfile

class TutorProfileForm(forms.ModelForm):

    class Meta:
        model = TutorProfile
        fields = '__all__'