from django.urls import path, include

from .views import MyRegisterFormView, pagelogin


urlpatterns = [
		path('login/', pagelogin, name="login"),
		path('signup/', MyRegisterFormView.as_view(), name='signup'),
	]
