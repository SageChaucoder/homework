# Generated by Django 4.2 on 2025-01-21 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='email',
            new_name='Email',
        ),
    ]
