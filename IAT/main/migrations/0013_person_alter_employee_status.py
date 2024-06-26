# Generated by Django 5.0.3 on 2024-05-16 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_employee_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Resigned', 'Resigned'), ('Supended', 'Suspended'), ('Terminated', 'Terminated'), ('Retired', 'Retired')], max_length=100),
        ),
    ]
