from django.urls import path
from .views import post_tutor

urlpatterns = [
    path('post-tutor/', post_tutor, name='post_tutor'),
]