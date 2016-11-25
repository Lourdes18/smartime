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
    url(r'^ver-alarma/(?P<pk>[0-9]+)$', smartime.views.show_alarm, name='show_alarm'),
    url(r'^modificar-alarma/(?P<pk>[0-9]+)$', smartime.views.edit_alarm, name='edit_alarm'),
    url(r'^eliminar-alarma/(?P<pk>[0-9]+)$', smartime.views.remove_alarm, name='remove_alarm'),

    #Configuraciones
    url(r'^ver-configuraciones$', smartime.views.show_settings, name='show_settings'),
    url(r'^nueva-configuracion$', smartime.views.new_setting, name='new_setting'),
    url(r'^ver-configuracion/(?P<pk>[0-9]+)$', smartime.views.show_setting, name='show_setting'),
    url(r'^modificar-configuracion/(?P<pk>[0-9]+)$', smartime.views.edit_setting, name='edit_setting'),
    url(r'^eliminar-configuracion/(?P<pk>[0-9]+)$', smartime.views.remove_setting, name='remove_setting'),

    #Eventos
    url(r'^ver-eventos$', smartime.views.show_events, name='show_events'),
    url(r'^nuevo-evento$', smartime.views.new_event, name='new_event'),
    url(r'^ver-evento/(?P<pk>[0-9]+)$', smartime.views.show_event, name='show_event'),
    url(r'^modificar-evento/(?P<pk>[0-9]+)$', smartime.views.edit_event, name='edit_event'),
    url(r'^eliminar-evento/(?P<pk>[0-9]+)$', smartime.views.remove_event, name='remove_event'),

    #Tareas
    url(r'^ver-tareas$', smartime.views.show_homeworks, name='show_homeworks'),
    url(r'^nueva-tarea$', smartime.views.new_homework, name='new_homework'),
    url(r'^ver-tarea/(?P<pk>[0-9]+)$', smartime.views.show_homework, name='show_homework'),
    url(r'^modificar-tarea/(?P<pk>[0-9]+)$', smartime.views.edit_homework, name='edit_homework'),
    url(r'^eliminar-tarea/(?P<pk>[0-9]+)$', smartime.views.remove_homework, name='remove_homework'),
]
