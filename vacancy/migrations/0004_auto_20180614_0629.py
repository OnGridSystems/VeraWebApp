# Generated by Django 2.0.3 on 2018-06-14 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0003_auto_20180614_0629'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profileonvacancy',
            old_name='cv',
            new_name='profile',
        ),
    ]
