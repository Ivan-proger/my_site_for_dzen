from django.shortcuts import render
from .models import Article


def home(request):
	article = Article.objects.all()
	return render(request, 'home.html', {'article' : article})

def redaction_article(request, date, id):
	article = Article.objects.all()
	return render(request, 'redaction/redaction.html', {'article' : article})