import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView

import requests
import base64



# Create your views here.

def index(request):
  with open('/usr/src/app/django-example/local/saml/key', 'rb') as f:
    secret_key = str(base64.b64encode(f.read()), 'utf-8')

  r = requests.get('https://api.darksky.net/forecast/'+secret_key+'/42.280826,-83.743038')
  return render(request, 'index.html', {'weatherString': r.text, 'key': secret_key})

def health(request):
  return HttpResponse(PageView.objects.count())
