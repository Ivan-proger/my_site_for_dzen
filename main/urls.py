from django.urls import path
from django.conf.urls import url
from .views import home


urlpatterns = [
	path('', home, name='home')
]