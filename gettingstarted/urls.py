from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import smartime.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
	
	#Vistas principales
    url(r'^$', smartime.views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),

    #Alarmas
    url(r'^ver-alarmas$', smartime.views.show_alarms, name='show_alarms'),
    url(r'^nueva-alarma$', smartime.views.new_alarm, name='new_alarm'),

    #Configuraciones
    url(r'^ver-configuraciones$', smartime.views.show_settings, name='show_settings'),
    url(r'^nueva-configuracion$', smartime.views.new_setting, name='new_setting'),

    #Eventos
    url(r'^ver-eventos$', smartime.views.show_events, name='show_events'),
    url(r'^nuevo-evento$', smartime.views.new_event, name='new_event'),

    #Tareas
    url(r'^ver-tareas$', smartime.views.show_homeworks, name='show_homeworks'),
    url(r'^nueva-tarea$', smartime.views.new_homework, name='new_homework'),
]
