# Generated by Django 3.1.1 on 2020-10-01 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesTaches', '0003_auto_20200930_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='created_date',
        ),
    ]
