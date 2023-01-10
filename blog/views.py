from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from django.utils import timezone
from blog.models import Article

# Create your views here.
def index(request):
    if request.method == 'POST':
        article = Article(title=request.POST['title'],
        body=request.POST['text'])
        article.save()
        context={"article":article,}
        return render(request, 'blog/detail.html', context)
    
    else:
        context = {
            "articles": Article.objects.all()
        }
        return render(request, 'blog/index.html', context)

def update(request, article_id):
    context = {
        "article_id": article_id
    }
    return render(request, "blog/tbd.html", context)

def detail(request, article_id):
    try:
        article=Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
	    raise Http404("Article does not exist")
    context = { 'article' : article }
    return render(request, "blog/detail.html", context)

def delete(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	article.delete()
	return redirect(index)

def create(request):
	return render(request, "blog/newPost.html")

def like(request, article_id):
	try:
		article=Article.objects.get(pk=article_id)
		article.like += 1
		article.save()
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	return redirect(detail, article_id)

def api_like(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
		article.like += 1
		article.save()
	except Article.DoesNotExist:
		raise Http404("Article does not exist")

	result = {
		'id' : article_id,
		'like' : article.like
	}

	return JsonResponse(result)