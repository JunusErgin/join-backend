# Generated by Django 3.2.9 on 2022-05-27 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='group',
            field=models.CharField(default='UNSET', max_length=6),
        ),
    ]
