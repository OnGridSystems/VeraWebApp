# Generated by Django 2.0.2 on 2018-03-05 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0029_auto_20180305_0603'),
        ('vacancy', '0008_auto_20180302_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='VacancyOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv.CurriculumVitae')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancy.Vacancy')),
            ],
        ),
    ]