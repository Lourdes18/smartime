from django import forms
from django.forms import ModelForm, Textarea
import datetime
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import widgets  

from .models import Alarm, Setting, Event, Homework


class AlarmForm(forms.ModelForm):
	class Meta:
		model = Alarm
		fields = ('date_alarm', 'time_alarm',)
		labels = {
            'date_alarm': _('Dia'),
            'time_alarm': _('Hora'),
        }



class SettingForm(forms.ModelForm):
	class Meta:
		model = Setting
		fields = ('title_setting', 'volumen_setting', 'vibration_setting',)
		labels = {
            'title_setting': _('Configuracion'),
            'volumen_setting': _('Volumen'),
            'vibration_setting': _('Vibracion'),
        }

class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = ('title_event', 'date_event', 'time_event', 'duration_event', 
				  'place_event', 'setting_event', )
		labels = {
            'title_event': _('Evento'),
            'date_event': _('Fecha'),
            'time_event': _('Hora'),
            'duration_event': _('Duracion'),
            'place_event': _('Longitud'),
            'setting_event': _('Configuracion'),
        }

class HomeworkForm(forms.ModelForm):
	class Meta:
		model = Homework
		fields = ('title_homework', 'description_homework', 'date_homework', 'time_homework', 
				  'priority_homework',)
		labels = {
            'title_homework': _('Evento'),
            'description_homework': _('Fecha'),
            'date_homework': _('Hora'),
            'time_homework': _('Duracion'),
            'priority_homework': _('Longitud'),
        }