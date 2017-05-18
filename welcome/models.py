from django.db import models

# Create your models here.

class PageView(models.Model):
  hostname = models.CharField(max_length=32)
  timestamp = models.DateTimeField(auto_now_add=True)

class ExpenseAccount(models.Model):
  name = models.CharField(max_length=30)
  total = models.DecimalField(max_digits=20,decimal_places=2)

  def __str__(self):
    return self.name

class ExpenseCategory(models.Model):
  name = models.CharField(max_length=30)
  total = models.DecimalField(max_digits=20,decimal_places=2)
  account = models.ForeignKey(ExpenseAccount)


  def __str__(self):
    return self.name

class ExpenseItem(models.Model):
  description = models.CharField(max_length=30)
  charge_codes = models.CharField(max_length=30)
  rate = models.DecimalField(max_digits=20,decimal_places=2)
  avg_monthly_units_billed = models.DecimalField(max_digits=20,decimal_places=1)
  billed_units = models.IntegerField()
  total = models.DecimalField(max_digits=20,decimal_places=2)

  category = models.ForeignKey(ExpenseCategory)
  

  def __str__(self):
    return self.description


