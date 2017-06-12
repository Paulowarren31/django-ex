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

  query = "select * from um_ecomm_dept_units_rept where ROWID IN ( SELECT MAX(ROWID) FROM um_ecomm_dept_units_rept GROUP BY dept_grp)"

  dic['dept_grp'] = cursor.execute(query).fetchall()

  query = "select * from um_ecomm_dept_units_rept where ROWID IN ( SELECT MAX(ROWID) FROM um_ecomm_dept_units_rept GROUP BY dept_grp_vp_area)"

  vp_area = cursor.execute(query).fetchall()

  dic['vp'] = vp_area

  query = "select * from um_ecomm_dept_units_rept where ROWID IN ( SELECT MAX(ROWID) FROM um_ecomm_dept_units_rept GROUP BY dept_bud_seq)"

  budget_seq = cursor.execute(query).fetchall()

  dic['bud_seq'] = budget_seq


  conn.close()

  return render(request, 'index.html', dic)

def table(request):

  conn = cx_Oracle.connect(connection_string)
  cursor = conn.cursor()

  query = "select * from um_ecomm_dept_units_rept where deptid='926200' and month BETWEEN 06 and 12 and calendar_yr between 2015 and 2016"

  rows = cursor.execute(query).fetchall()

  return render(request, 'table.html', {'rows': rows})

def secret(request):
  with open('/usr/src/app/myapp/local/saml/secret-key', 'rb') as f:
    secret_key = str(base64.b64encode(f.read()), 'utf-8')
    return render(request, 'secret.html', {'key': secret_key})

def profile(request):
  return render(request, 'index.html')
