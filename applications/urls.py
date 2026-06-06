from django.urls import path
from .views import apply_tuition

urlpatterns = [
    path(
    'my-applications/',
    my_applications,
    name='my_applications'
),
]