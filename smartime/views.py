from django.shortcuts import render
from django.http import HttpResponse
from smartime.forms import AlarmForm
from .models import User, Alarm, Setting, Event, Homework



# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

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

