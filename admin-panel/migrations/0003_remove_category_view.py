# Generated by Django 3.1.3 on 2020-11-04 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin-panel', '0002_category_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='view',
        ),
    ]
