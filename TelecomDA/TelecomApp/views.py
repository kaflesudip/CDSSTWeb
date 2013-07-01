# Create your views here.
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from models import *


def home(request):
    sliders = HomeSlider.objects.all()
    home_content = HomeContent.objects.all()
    parameters = {}
    parameters["slider"] = sliders
    parameters["home_content"] = home_content
    return render_to_response('home.html', parameters)


def overview(request):
    overviews = Overview.objects.all()
    parameters = {}
    parameters["overviews"] = overviews
    return render_to_response('overview.html', parameters)


def output(request):
    screenshots = Screenshot.objects.all()
    parameters = {}
    parameters["screenshots"] = screenshots
    return render_to_response('screenshot.html', parameters)


def tools(request):
    tools = Tool.objects.all()
    parameters = {}
    parameters["tools"] = tools
    return render_to_response('tools.html', parameters)


def team(request):
    teams = Team.objects.all()
    parameters = {}
    parameters["teams"] = teams
    return render_to_response('team.html', parameters)
