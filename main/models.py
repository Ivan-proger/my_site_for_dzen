from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

class Article(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField('заголовок статьи', max_length=40, blank=True)
	description = models.CharField('описание статьи', max_length=150, blank=True)
	text = models.TextField('текст статьи', blank=True)
	time = models.DateTimeField(auto_now=True)
	likes = models.ManyToManyField(User, related_name='likes', blank=True)
	img = models.ImageField('превью', upload_to='images/', blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('redaction', kwargs={'date' : self.time.strftime('%Y%m%d'), 'id' : str(self.id)})
	
	class Meta():
		verbose_name = "статья"
		verbose_name_plural = "статьи"

class Photo(models.Model):
	img_data = models.ImageField(upload_to='photos')
	article = models.ForeignKey(Article, on_delete = models.CASCADE, related_name='all_phots')

	class Meta:
		verbose_name = "Фотография"
		verbose_name_plural = "Фотографии"