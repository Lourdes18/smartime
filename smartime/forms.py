from django import forms
from django.forms import ModelForm, Textarea
import datetime
from django.utils.translation import ugettext_lazy as _

from .models import User, Alarm, Setting, Event, Homework


class AlarmForm(forms.ModelForm):
	class Meta:
		model = Alarm
		fields = ('date_alarm',)
		
