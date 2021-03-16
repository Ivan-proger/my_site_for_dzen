from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

from .models import Article
from .forms import ArticleRed, ImgForm

def home(request):
	article = Article.objects.all()
	return render(request, 'home.html', {'article' : article})

def redaction_article(request, date, id, *args):
	if request.user.is_superuser:
		article = Article.objects.get(id=id)

		if 'img' in request.FILES:
			form = ImgForm(request.FILES)
			if request.user.is_superuser:
				article.img = request.FILES['img']
				img = request.FILES['img']
				article.user = request.user
				fs = FileSystemStorage()
				filename = fs.save(img.name, img)
				uploaded_file_url = fs.url(filename)
				article.save()
				return render(request, "redaction/redaction.html", {"form" : form, "uploaded_file_url" : uploaded_file_url})
			else:
				return render(request, "redaction/lox.html", {"error" : "У вас не хватает прав!"})

		if 'title' in request.POST and 'text' in request.POST:
			form1 = ArticleRed(request.POST)
			if request.user.is_superuser:
				article.title = request.POST['title']
				article.text = request.POST['text']
				article.user = request.user
				article.save()
				return render(request, "redaction/redaction.html", {"form1" : form1})
			else:
				return render(request, "redaction/redaction.html", {"error" : "у вас не хватает прав", 'article' : article})
		else:
			form = ImgForm()
			form1 = ArticleRed()
			print(request.POST)
			return render(request, "redaction/redaction.html", {"form1" : form1, "form" : form, "error" : "данные не действительные! form1____", 'article' : article})
	else:
		return render(request, "redaction/lox.html", {"error" : "У вас не хватает прав!"})
