from django.shortcuts import get_object_or_404
from .models import TuitionPost

def tuition_detail(request, pk):

    tuition = get_object_or_404(
        TuitionPost,
        pk=pk
    )

    return render(
        request,
        'tuition_detail.html',
        {
            'tuition': tuition
        }
    )