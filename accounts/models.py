from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="профиль")
	updated_on = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.user.username

	class Meta():
		verbose_name = "дата228"