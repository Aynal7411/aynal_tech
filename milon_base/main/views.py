from django.shortcuts import render
from .models import Project, Skill
from .forms import ContactForm

def home(request):
    skills = Skill.objects.all()
    return render(request, 'home.html', {'skills': skills})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})