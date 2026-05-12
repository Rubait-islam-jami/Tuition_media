from django import forms
from .models import TuitionPost

class TuitionPostForm(forms.ModelForm):

    class Meta:
        model = TuitionPost
        fields = '__all__'