from django.urls import path
from django.conf.urls import url
from .views import home, redaction_article


urlpatterns = [
	path('', home, name='home'),
	path('red/<int:date><int:id>', redaction_article, name='redaction'),
]