# Generated by Django 3.1.3 on 2020-11-30 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artifacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='location_text',
            new_name='text',
        ),
    ]