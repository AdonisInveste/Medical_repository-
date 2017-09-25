from django.conf.urls import url 
from home.views import Identity_view
from . import views

urlpatterns = [
	url(r'^$', Identity_view.as_view(), name = 'home'),
#	url(r'^patient-profile/$', views.patient_profile, name = 'patient_profile'),
]