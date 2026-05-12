from django.shortcuts import render, redirect
from .forms import TuitionPostForm

def post_tuition(request):

    form = TuitionPostForm()

    if request.method == 'POST':

        form = TuitionPostForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/')

    return render(request, 'post_tuition.html', {'form': form})