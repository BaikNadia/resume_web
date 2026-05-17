from django.shortcuts import render, redirect
from .models import Service, Project
from .forms import RequestForm


def home(request):
    services = Service.objects.all()
    projects = Project.objects.all().order_by('-created_at')[:6]  # последние 6 работ

    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            # Можно добавить сообщение об успехе
            return redirect('home')
    else:
        form = RequestForm()

    return render(request, 'main/home.html', {
        'services': services,
        'projects': projects,
        'form': form,
    })
