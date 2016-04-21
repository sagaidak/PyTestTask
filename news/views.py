from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from news.models import Article

# Create your views here.


@csrf_exempt
def home(request):
    list_n = 5      # Number of list items
    articles_list = Article.objects.filter(is_published=True)[:list_n]

    if request.is_ajax():
        mimetype = 'application/javascript'
        i = int(request.POST['iteration'])
        i_plus = i + 5

        articles_list = Article.objects.filter(is_published=True)[i:i_plus]
        data = serializers.serialize('json', articles_list)

        return HttpResponse(data, mimetype)
    else:
        context = {'articles_list': articles_list}
        return render(request, 'news/home.html', context)


def article_page(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'news/article.html', {'article': article})



