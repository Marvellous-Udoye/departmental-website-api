# Generated by Django 5.1.3 on 2025-01-06 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='phonenumber',
            new_name='level',
        ),
    ]
