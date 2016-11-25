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
]
