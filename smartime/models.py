from django.db import models
from decimal import Decimal
from django.utils.timezone import now
from uuid import uuid4
from django.db import IntegrityError

# Crear modelos para la base de datos


class User(models.Model):
    name_user = models.CharField(max_length=100, unique= True)
    email_user = models.CharField(max_length=1000)
    pass_user = models.CharField(max_length=100)
    long_user = models.DecimalField(max_digits=25,decimal_places=2,default=Decimal('0.00'))
    latitud_user = models.DecimalField(max_digits=25,decimal_places=2,default=Decimal('0.00'))

    def __str__(self):              # __unicode__ on Python 2
        return "%s %s %s %d %d" % (self.name_user, self.email_user, self.pass_user, self.long_user, self.latitud_user)

class Alarm(models.Model):
	date_alarm = models.DateField()
	time_alarm = models.TimeField()
	user_alarm = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", to_field=('id'))

	def __str__(self):              # __unicode__ on Python 2
		return "%s" % (str(self.date_alarm), str(self.time_alarm))


class Setting(models.Model):
	CHOICE = (
        ('No', 'Sin vibracion'),
        ('Si', 'Con vibracion'),
    )
	title_setting = models.CharField(max_length=100, unique= True)
	volumen_setting =models.IntegerField()
	vibration_setting = models.CharField(max_length=2, choices=CHOICE)

	def __str__(self):              # __unicode__ on Python 2
		return " %s, %i, %s " % (self.title_setting, self.volumen_setting, self.vibration_setting)

class Event(models.Model):
	title_event = models.CharField(max_length=100)
	date_event = models.DateField()
	time_event = models.TimeField()
	duration_event = models.TimeField()
	volumen_setting =models.IntegerField()
	long_event = models.DecimalField(max_digits=25,decimal_places=2,default=Decimal('0.00'))
	latitud_event = models.DecimalField(max_digits=25,decimal_places=2,default=Decimal('0.00'))
	user_event = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userid", to_field=('id'))
	setting_event = models.ForeignKey(Setting, on_delete=models.CASCADE, related_name="setting", to_field=('id'))


	def __str__(self):              # __unicode__ on Python 2
		return " %s, %s, %s, %s, %i, %d, %d " % (self.title_event, str(self.date_event), str(self.time_event), str(self.duration_event), self.volumen_setting, self.long_event, self.latitud_event)

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

	def __str__(self):              # __unicode__ on Python 2
		return " %s, %s, %s, %s, %s" % (self.title_homework, self.description_homework, str(self.date_event), str(self.time_homework), self.priority_homework)







