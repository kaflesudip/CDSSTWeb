# Create your views here.
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
import datetime

def home(request):
	return render_to_response('home.html')