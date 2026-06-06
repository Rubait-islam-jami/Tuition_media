from django.urls import path
from .views import apply_tuition, my_applications

urlpatterns = [
    path(
        'apply/<int:tuition_id>/',
        apply_tuition,
        name='apply_tuition'
    ),

    path(
        'my-applications/',
        my_applications,
        name='my_applications'
    ),
]