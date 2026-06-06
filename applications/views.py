from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import ApplicationForm
from .models import Application

from tuition.models import TuitionPost
from tutors.models import TutorProfile


@login_required
def apply_tuition(request, tuition_id):

    tuition = get_object_or_404(
        TuitionPost,
        id=tuition_id
    )

    tutor = get_object_or_404(
        TutorProfile,
        user=request.user
    )

    if request.method == 'POST':

        form = ApplicationForm(request.POST)

        if form.is_valid():

            application = form.save(commit=False)

            application.tutor = tutor
            application.tuition = tuition

            application.save()

            return redirect('/')

    else:

        form = ApplicationForm()

    return render(
        request,
        'apply_tuition.html',
        {
            'form': form,
            'tuition': tuition
        }
    )


@login_required
def my_applications(request):

    tutor = TutorProfile.objects.get(
        user=request.user
    )

    applications = Application.objects.filter(
        tutor=tutor
    )

    return render(
        request,
        'my_applications.html',
        {
            'applications': applications
        }
    )