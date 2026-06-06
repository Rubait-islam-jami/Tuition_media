from django.contrib import admin
from .models import TutorProfile

@admin.register(TutorProfile)
class TutorProfileAdmin(admin.ModelAdmin):

    list_display = (
        'full_name',
        'university',
        'subject'
    )