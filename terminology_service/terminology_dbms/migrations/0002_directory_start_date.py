# Generated by Django 3.2.10 on 2021-12-26 11:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terminology_dbms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='directory',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]