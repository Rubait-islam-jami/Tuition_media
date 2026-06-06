from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import TuitionPostForm
from .models import TuitionPost


def home(request):

    tuitions = TuitionPost.objects.all().order_by('-created_at')

    return render(
        request,
        'home.html',
        {
            'tuitions': tuitions
        }
    )


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


@login_required
def post_tuition(request):

    if request.method == 'POST':

        form = TuitionPostForm(request.POST)

        if form.is_valid():

            tuition = form.save(commit=False)
            tuition.user = request.user
            tuition.save()

            return redirect('/')

    else:

        form = TuitionPostForm()

    return render(
        request,
        'post_tuition.html',
        {
            'form': form
        }
    )