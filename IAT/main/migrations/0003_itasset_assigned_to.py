# Generated by Django 5.0.3 on 2024-04-30 04:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_itasset_rename_birth_date_employee_hire_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='itasset',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.employee'),
        ),
    ]
