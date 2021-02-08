from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
	title = models.CharField('заголовок статьи', max_length=200)
	text = models.TextField('текст статьи')
	time = models.DateTimeField(auto_now=True)
	likes = models.ManyToManyField(User, related_name='likes')

	def __str__(self):
		return self.title

	class Meta():
		verbose_name = "статья"
		verbose_name_plural = "статьи"