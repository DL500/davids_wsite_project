from django.shortcuts import render
from .models import Project

def home(request):
	projects = Project.objects.all()
	return render(request, 'wsite/home.html', {'projects':projects})

def knowledgeTile(request):
	return render(request, 'wsite/knowledgeTile.html')

