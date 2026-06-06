from django.urls import path
from .views import home, post_tuition, tuition_detail

urlpatterns = [
    path('', home, name='home'),
    path('post-tuition/', post_tuition, name='post_tuition'),
    path('tuition/<int:pk>/', tuition_detail, name='tuition_detail'),
]