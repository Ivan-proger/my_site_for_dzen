from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

from .models import Article
from .forms import PreviewForm

def home(request):
	article = Article.objects.all()
	return render(request, 'home.html', {'article' : article})

def redaction_article(request, date, id, *args):
	form = PreviewForm(request.POST, request.FILES)
	if request.method == "POST":
		if form.is_valid():
			try:
				article = Article.objects.get(id=id)
				article.user = request.user
				img = request.FILES['img']
				article.img = img
				fs = FileSystemStorage()
				filename = fs.save(img.name, img)
				uploaded_file_url = fs.url(filename)
				article.save()
				return render(request, "redaction/redaction.html", {"form" : form, "uploaded_file_url" : uploaded_file_url})

			except Article.DoesNotExist:
				return render(request, "redaction/redaction.html", {"form" : form, "error" : "такой статьи не существует!", 'article' : article})
			except:
				return render(request, "redaction/redaction.html", {"form" : form, "error" : "что то пошло не так =(", 'article' : article})

		else:
			return render(request, "redaction/redaction.html", {"form" : form, "error" : "не удаётся загрузить картинку!", 'article' : article})
	else:
		return render(request, "redaction/redaction.html", {"form" : form, "error" : "данные не действительные!"})

