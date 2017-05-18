import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView

import requests



# Create your views here.

def index(request):
  f = open('/usr/src/app/django-example/local/saml/key', 'r')
  #b = f.read()
  #r = requests.get('https://api.darksky.net/forecast/'+os.environ['KEY']+'/42.280826,-83.743038')
  return render(request, 'index.html', {'weatherString': 'asd', 'key': 'hello'})

def health(request):
  return HttpResponse(PageView.objects.count())
