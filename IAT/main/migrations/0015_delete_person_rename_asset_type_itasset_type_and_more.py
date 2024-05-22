# Generated by Django 5.0.3 on 2024-05-16 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_person_email_person_city'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.RenameField(
            model_name='itasset',
            old_name='asset_type',
            new_name='type',
        ),
        migrations.AddField(
            model_name='itasset',
            name='request_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='hire_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]