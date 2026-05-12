from django.urls import path
from .views import post_tuition

urlpatterns = [
    path('post-tuition/', post_tuition, name='post_tuition'),
]