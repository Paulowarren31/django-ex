# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('total', models.DecimalField(max_digits=20, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('total', models.DecimalField(max_digits=20, decimal_places=2)),
                ('account', models.ForeignKey(to='welcome.ExpenseAccount')),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=30)),
                ('charge_codes', models.CharField(max_length=30)),
                ('rate', models.DecimalField(max_digits=20, decimal_places=2)),
                ('avg_monthly_units_billed', models.DecimalField(max_digits=20, decimal_places=1)),
                ('billed_units', models.IntegerField()),
                ('total', models.DecimalField(max_digits=20, decimal_places=2)),
                ('category', models.ForeignKey(to='welcome.ExpenseCategory')),
            ],
        ),
        migrations.CreateModel(
            name='PageView',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=32)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
