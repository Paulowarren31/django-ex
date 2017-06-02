import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from . import database
from .models import PageView, ExpenseAccount

import requests
import base64


# Create your views here.

#@login_required(login_url='/accounts/login')
def index(request):
  return render(request, 'index.html')

def table(request):
  accounts = ExpenseAccount.objects.all()
   #account.expensecategory_set.all()

  for account in accounts:
    categories = account.expensecategory_set.all()
    account.categories = categories

    for category in categories:
      items = category.expenseitem_set.all()
      category.items = items

  return render(request, 'table.html', {'accounts': accounts})

def secret(request):
  with open('/usr/src/app/myapp/local/saml/secret-key', 'rb') as f:
    secret_key = str(base64.b64encode(f.read()), 'utf-8')
    return render(request, 'secret.html', {'key': secret_key})

def profile(request):
  return render(request, 'index.html')
