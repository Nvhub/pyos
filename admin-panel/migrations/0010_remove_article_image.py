# Generated by Django 3.1.3 on 2020-11-12 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin-panel', '0009_auto_20201111_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
    ]