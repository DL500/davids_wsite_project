from django.shortcuts import render
from .models import Project
import datetime

def home(request):
	"""
	this will deal with the projects created and
	the temp. Covid roadmap countdown
	"""
	s1 = datetime.datetime(2021,3,8) - datetime.datetime.now()
	s1B = datetime.datetime(2021,3,29) - datetime.datetime.now()
	s2 = datetime.datetime(2021,4,12) - datetime.datetime.now()
	s3 = datetime.datetime(2021,5,17) - datetime.datetime.now()
	s4 = datetime.datetime(2021,6,21) - datetime.datetime.now()

	projects = Project.objects.all()
	
	return render(request, 'wsite/home.html', {'projects':projects,'s1':s1, 's1B':s1B, 's2':s2, 's3':s3, 's4':s4})

def knowledgeTile(request):
	return render(request, 'wsite/knowledgeTile.html')

def nct(request):
	"""
    this has temporarilly taken place of blog project link on landing page
	"""
	beer = datetime.datetime(2021,4,23) - datetime.datetime.now()
	return render(request, 'wsite/nct.html', {'beer':beer})

