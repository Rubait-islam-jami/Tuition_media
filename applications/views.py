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