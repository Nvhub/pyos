# Generated by Django 3.1.3 on 2020-11-04 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin-panel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='view',
            field=models.IntegerField(default=1),
        ),
    ]
