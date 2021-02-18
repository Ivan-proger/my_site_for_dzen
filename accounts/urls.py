from django.urls import path, include

from .views import MyRegisterFormView, pagelogin, validcode


urlpatterns = [
		path('code/', validcode, name="code"),
		path('login/', pagelogin, name="login"),
		path('signup/', MyRegisterFormView.as_view(), name='signup'),
	]
