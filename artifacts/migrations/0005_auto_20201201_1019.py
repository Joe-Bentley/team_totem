# Generated by Django 3.1.3 on 2020-12-01 10:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artifacts', '0004_auto_20201201_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artifact',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Date Published'),
        ),
    ]
