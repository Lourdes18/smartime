# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_alarm', models.DateField()),
                ('time_alarm', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title_event', models.CharField(max_length=100)),
                ('date_event', models.DateField()),
                ('time_event', models.TimeField()),
                ('duration_event', models.TimeField()),
                ('place_event', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title_homework', models.CharField(max_length=100)),
                ('description_homework', models.CharField(max_length=1000)),
                ('date_homework', models.DateField()),
                ('time_homework', models.TimeField()),
                ('priority_homework', models.CharField(max_length=25, choices=[(b'1', b'Sin'), (b'2', b'Baja'), (b'3', b'Media'), (b'4', b'Alta')])),
                ('event_homework', models.ForeignKey(related_name='event', to='smartime.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title_setting', models.CharField(unique=True, max_length=100)),
                ('volumen_setting', models.CharField(max_length=2, choices=[(b'Sin sonido', b'0%'), (b'Interior', b'20%'), (b'Bajo', b'40%'), (b'Medio', b'60%'), (b'Alto', b'80%'), (b'Exterior', b'100%')])),
                ('vibration_setting', models.CharField(max_length=2, choices=[(b'No', b'Sin vibracion'), (b'Si', b'Con vibracion')])),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email_user', models.CharField(max_length=1000)),
                ('pass_user', models.CharField(max_length=100)),
                ('location_user', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='event_homework',
            field=models.ForeignKey(related_name='event', to='smartime.Event'),
        ),
        migrations.AddField(
            model_name='event',
            name='setting_event',
            field=models.ForeignKey(related_name='setting', to='smartime.Setting'),
        ),
        migrations.AddField(
            model_name='event',
            name='user_event',
            field=models.ForeignKey(related_name='userid', default=1, to='smartime.User'),
        ),
        migrations.AddField(
            model_name='alarm',
            name='user_alarm',
            field=models.ForeignKey(related_name='user', default=1, to='smartime.User'),
        ),
    ]
