from django.urls import path, include

from .views import MyRegisterFormView


urlpatterns = [
		path('signup/', MyRegisterFormView.as_view(), name='signup'),
	]
