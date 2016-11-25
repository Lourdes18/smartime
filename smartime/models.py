from django.db import models
from decimal import Decimal
from django.utils.timezone import now
from uuid import uuid4
from django.db import IntegrityError

# Crear modelos para la base de datos


class User(models.Model):
	name_user = models.CharField(max_length=50)
	email_user = models.CharField(max_length=1000)
	pass_user = models.CharField(max_length=100)
	location_user = models.CharField(max_length=1000)

	def __str__(self):              # __unicode__ on Python 2
		return "%s %s %s %s" % (self.name_user, self.email_user, self.pass_user, self.location_user)

class Alarm(models.Model):
	date_alarm = models.DateField()
	time_alarm = models.TimeField()
	user_alarm = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", to_field=('id'), default = 1)

	def __str__(self):              # __unicode__ on Python 2
		return "%s" % (str(self.date_alarm), str(self.time_alarm))


class Setting(models.Model):
	SOUND = (
    	('Sin sonido', '0%'),
        ('Interior', '20%'),
        ('Bajo', '40%'),
        ('Medio', '60%'),
        ('Alto', '80%'),
        ('Exterior', '100%'),
    )

	CHOICE = (
        ('No', 'Sin vibracion'),
        ('Si', 'Con vibracion'),
    )
	title_setting = models.CharField(max_length=100, unique= True)
	volumen_setting = models.CharField(max_length=15, choices=SOUND)
	vibration_setting = models.CharField(max_length=5, choices=CHOICE)

	def __str__(self):              # __unicode__ on Python 2
		return " %s %s %s " % (self.title_setting, self.volumen_setting, self.vibration_setting)

class Event(models.Model):

	title_event = models.CharField(max_length=100)
	date_event = models.DateField()
	time_event = models.TimeField()
	duration_event = models.TimeField()
	place_event = models.CharField(max_length=100)
	user_event = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userid", to_field=('id'), default = 1)
	setting_event = models.ForeignKey(Setting, on_delete=models.CASCADE, related_name="setting", to_field=('id'))


	def __str__(self):              # __unicode__ on Python 2
		return " %s %s %s %s %s " % (self.title_event, str(self.date_event), str(self.time_event), str(self.duration_event), self.volumen_setting, self.place_event)

class Homework(models.Model):
	CHOICE = (
        ('1', 'Sin'),
        ('2', 'Baja'),
        ('3', 'Media'),
        ('4', 'Alta'),
    )
	title_homework = models.CharField(max_length=100)
	description_homework = models.CharField(max_length=1000)
	date_homework = models.DateField()
	time_homework =models.TimeField()
	priority_homework = models.CharField(max_length=25, choices=CHOICE)
	event_homework = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="event", to_field=('id'))


	def __str__(self):              # __unicode__ on Python 2
		return " %s, %s, %s, %s, %s" % (self.title_homework, self.description_homework, str(self.date_event), str(self.time_homework), self.priority_homework)







