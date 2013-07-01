# Create your views here.
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
import datetime

def home(request):
	return render_to_response('home.html')

def overview(request):
	return render_to_response('overview.html')

def output(request):
	return render_to_response('output.html')

def tools(request):
	return render_to_response('tools.html')

def team(request):
	return render_to_response('team.html')
