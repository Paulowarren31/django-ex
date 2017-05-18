import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView, ExpenseAccount

import requests
import base64


# Create your views here.

def index(request):
  accounts = ExpenseAccount.objects.all()
   #account.expensecategory_set.all()

  for account in accounts:
    categories = account.expensecategory_set.all()
    account.categories = categories

    for category in categories:
      items = category.expenseitem_set.all()
      category.items = items

  return render(request, 'index.html', {'accounts': accounts})

def secret(request):
  with open('/usr/src/app/django-example/local/saml/key', 'rb') as f:
    secret_key = str(base64.b64encode(f.read()), 'utf-8')
    return render(request, 'secret.html', {'key': secret_key})

