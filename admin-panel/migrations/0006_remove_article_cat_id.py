# Generated by Django 3.1.3 on 2020-11-11 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin-panel', '0005_auto_20201109_0951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='cat_id',
        ),
    ]
