# Generated by Django 3.2.20 on 2023-08-15 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_apply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='job',
            name='start_date',
        ),
    ]
