from django import forms
from django.contrib.auth.models import User

class ArticleRed(forms.Form):
	title = forms.CharField(required=True, label='title', max_length=55)
	text = forms.CharField(required=True, label='title', max_length=60000)

	def __str__(self):
		return self.title, self.text

class PreviewForm(forms.Form):
	img = forms.FileField()
