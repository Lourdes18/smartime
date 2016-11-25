from django.contrib import admin
from .models import User, Alarm, Setting, Event, Homework


# Register your models here.
admin.site.register(User)
admin.site.register(Alarm)
admin.site.register(Setting)
admin.site.register(Event)
admin.site.register(Homework)

