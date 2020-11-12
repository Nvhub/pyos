from django.shortcuts import render, HttpResponseRedirect
from ..models import Article
from ..settings.forms import ArticleForm
from django.views.generic import CreateView, UpdateView
from ..settings.mixins import access_required


@access_required
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    template_name = 'admin-panel\\article\index.html'
    return render(request, template_name, context)


@access_required
def show(request, id):
    article = Article.objects.get(id=id)
    context = {'article': article}
    return render(request, 'admin-panel\\article\show.html', context)


# TODO change to functional
class create(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'admin-panel\\article\create_update.html'
    success_url = '/article'


class update(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'admin-panel\\article\create_update.html'
    success_url = '/article'


@access_required
def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))