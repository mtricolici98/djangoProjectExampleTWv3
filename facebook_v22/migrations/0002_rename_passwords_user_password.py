# Generated by Django 4.2.4 on 2023-08-11 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facebook_v22', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='passwords',
            new_name='password',
        ),
    ]
