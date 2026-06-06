from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('tuition.urls')),
    path('', include('tutors.urls')),
    path('', include('applications.urls')),

    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]