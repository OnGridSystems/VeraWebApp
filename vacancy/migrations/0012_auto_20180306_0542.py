# Generated by Django 2.0.2 on 2018-03-06 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0011_auto_20180305_1201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacancy',
            old_name='specializations',
            new_name='specialisations',
        ),
    ]