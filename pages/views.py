from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from .models import Article, Tag


def index(request):
    context = {}
    return render(request, 'page-index.html', context)

def vlist(request):
    articles = Article.objects.all()
    tags = Tag.objects.all()
    context = {
        'article_list': articles,
        'tag_list': tags
    }
    return render(request, 'article/list.html', context)

def detail(request, article_id):
    article_set = Article.objects.filter(id=article_id)
    if article_set.count()>0:
        article = article_set.first()
        context = {
            'article': article
        }
        return render(request, 'article/detail.html', context)
    raise Http404("没有此页面！")
def search(request):
    context = {}
    return render(request, 'article/search.html', context)
def copyright(request):
    context = {}
    return render(request, 'me/copyright.html', context)
def about(request):
    context = {}
    return render(request, 'me/about.html', context)
def message(request):
    context = {}
    return render(request, 'me/message.html', context)