import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from . import database

import requests
import base64
import cx_Oracle #oracle DB lib

connection_string = 'paulowar/Pw6517nP@pinntst.dsc.umich.edu:1521/pinndev.world'

# Create your views here.

@login_required(login_url='/accounts/login')
def index(request):
  dic = {}

  conn = cx_Oracle.connect(connection_string)
  cursor = conn.cursor()

  query = "select * from um_ecomm_dept_units_rept where ROWID IN ( SELECT MAX(ROWID) FROM um_ecomm_dept_units_rept GROUP BY dept_grp_vp_area)"

  vp_area = cursor.execute(query)

  dic['vp'] = vp_area

  query = "select * from um_ecomm_dept_units_rept where ROWID IN ( SELECT MAX(ROWID) FROM um_ecomm_dept_units_rept GROUP BY dept_bud_seq)"

  budget_seq = cursor.execute(query)

  dic['bud_seq'] = budget_seq

  return render(request, 'index.html', dic)

#def table(request):
#  accounts = ExpenseAccount.objects.all()
#   #account.expensecategory_set.all()
#
#  for account in accounts:
#    categories = account.expensecategory_set.all()
#    account.categories = categories
#
#    for category in categories:
#      items = category.expenseitem_set.all()
#      category.items = items
#
#  return render(request, 'table.html', {'accounts': accounts})

def secret(request):
  with open('/usr/src/app/myapp/local/saml/secret-key', 'rb') as f:
    secret_key = str(base64.b64encode(f.read()), 'utf-8')
    return render(request, 'secret.html', {'key': secret_key})

def profile(request):
  return render(request, 'index.html')
