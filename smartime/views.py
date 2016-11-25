from django.shortcuts import render
from django.http import HttpResponse
from smartime.forms import AlarmForm, SettingForm, EventForm, HomeworkForm
from .models import User, Alarm, Setting, Event, Homework



# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

#SCRUD alarmas
def show_alarms(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'alarms/showAlarms.html')
    '''
    alarms = Alarm.objects.all()
    return render(request, 'alarms/showAlarms.html',{'alarms': alarms})
	'''

def new_alarm(request):
    if request.method == "POST":
        form = AlarmForm(request.POST)
        if form.is_valid():
            Alarm = form.save(commit=False)
            Alarm.author = request.user
            Alarm.save()
            form = AlarmForm()
            return HttpResponseRedirect('/ver-alarmas')

    else:
        form = AlarmForm()
    return render(request, 'alarms/newAlarm.html', {'form': form})

def show_alarm(request, pk):
    try: 
        alarm =  Alarm.objects.get(id = pk)
    except Alarm.DoesNotExist:
        alarm = None
    return render(request, 'alarms/showAlarm.html', {'alarm': alarm})

def edit_alarm(request, pk):
    try: 
        alarm = Alarm.objects.get(id = pk)
    except Alarm.DoesNotExist:
      alarm = None
    if request.method == "POST":
        form = AlarmForm(request.POST, instance=alarm)
        if form.is_valid():
            alarm = form.save(commit=False)
            alarm.author = request.user
            alarm.save()
            return HttpResponseRedirect('/ver-alarmas')
    else:
        form = AlarmForm(instance=alarm)
    return render(request, 'alamrs/editAlarm.html', {'form': form})


def remove_alarm(request, pk):
    try: 
        alarm = alarm.objects.get(id = pk)
        alarm.objects.filter(id = pk).delete()
    except alarm.DoesNotExist:
        alarm = None
    return HttpResponseRedirect('/ver-alarmas')


#SCRUD Configuraciones
def show_settings(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'settings/showSettings.html')
    '''
    settings = Setting.objects.all()
    return render(request, 'settings/showSetting.html',{'settings': settings})
    '''

def new_setting(request):
    if request.method == "POST":
        form = SettingForm(request.POST)
        if form.is_valid():
            Setting = form.save(commit=False)
            Setting.author = request.user
            Setting.save()
            form = SettingForm()
            return HttpResponseRedirect('/ver-configuraciones')

    else:
        form = SettingForm()
    return render(request, 'settings/newSetting.html', {'form': form})

def show_setting(request, pk):
    try: 
        setting =  Setting.objects.get(id = pk)
    except Setting.DoesNotExist:
        setting = None
    return render(request, 'settings/showSetting.html', {'setting': setting})

def edit_setting(request, pk):
    try: 
        setting = Setting.objects.get(id = pk)
    except Setting.DoesNotExist:
      setting = None
    if request.method == "POST":
        form = SettingForm(request.POST, instance=setting)
        if form.is_valid():
            setting = form.save(commit=False)
            setting.author = request.user
            setting.save()
            return HttpResponseRedirect('/ver-configuraciones')
    else:
        form = SettingForm(instance=setting)
    return render(request, 'settings/editSetting.html', {'form': form})


def remove_setting(request, pk):
    try: 
        setting = setting.objects.get(id = pk)
        setting.objects.filter(id = pk).delete()
    except setting.DoesNotExist:
        setting = None
    return HttpResponseRedirect('/ver-configuraciones')

#SCRUD Eventos
def show_events(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'events/showEvents.html')
    '''
    events = Event.objects.all()
    return render(request, 'events/showEvents.html',{'events': events})
    '''

def new_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            Event = form.save(commit=False)
            Event.author = request.user
            Event.save()
            form = EventForm()
            return HttpResponseRedirect('/ver-eventos')

    else:
        form = EventForm()
    return render(request, 'events/newEvent.html', {'form': form})

def show_event(request, pk):
    try: 
        event =  Setting.objects.get(id = pk)
    except Setting.DoesNotExist:
        event = None
    return render(request, 'settings/showSetting.html', {'event': event})

def edit_event(request, pk):
    try: 
        event = Setting.objects.get(id = pk)
    except Setting.DoesNotExist:
      event = None
    if request.method == "POST":
        form = SettingForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()
            return HttpResponseRedirect('/event')
    else:
        form = SettingForm(instance=event)
    return render(request, 'settings/editSetting.html', {'form': form})


def remove_event(request, pk):
    try: 
        event = event.objects.get(id = pk)
        event.objects.filter(id = pk).delete()
    except Event.DoesNotExist:
        event = None
    return HttpResponseRedirect('/ver-configuraciones')

#SCRUD tareas
def show_homeworks(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'homeworks/showHomeworks.html')
    '''
    homeworks = Homeworks.objects.all()
    return render(request, 'homeworks/showHomeworks.html',{'homeworks': homeworks})
    '''

def new_homework(request):
    if request.method == "POST":
        form = HomeworkForm(request.POST)
        if form.is_valid():
            Homework = form.save(commit=False)
            Homework.author = request.user
            Homework.save()
            form = HomeworkForm()
            return HttpResponseRedirect('/ver-tareas')

    else:
        form = HomeworkForm()
    return render(request, 'homeworks/newHomework.html', {'form': form})