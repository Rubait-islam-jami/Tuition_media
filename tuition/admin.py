from django.contrib import admin
from .models import TuitionPost

@admin.register(TuitionPost)
class TuitionPostAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'subject',
        'salary',
        'area'
    )