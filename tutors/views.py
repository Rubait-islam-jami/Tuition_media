from django.shortcuts import render, redirect
from .forms import TutorProfileForm

def post_tutor(request):

    form = TutorProfileForm()

    if request.method == 'POST':

        form = TutorProfileForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/')

    return render(request, 'post_tutor.html', {'form': form})