# Generated by Django 3.1.3 on 2020-11-09 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin-panel', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('e', 'enable'), ('d', 'disable')], default='e', max_length=1),
        ),
    ]