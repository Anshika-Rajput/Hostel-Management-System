# Generated by Django 4.0 on 2022-02-09 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_alter_contact_us_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact_us',
            name='date',
        ),
        migrations.RemoveField(
            model_name='contact_us',
            name='time',
        ),
    ]
