from django.shortcuts import render, HttpResponseRedirect
from ..models import Category
from ..settings.mixins import login_required,access_required
from ..settings.forms import CategoryForm
from ..settings.filters import CategoryFilter


@access_required
def index(request):

    categories = Category.objects.all()
    filters = CategoryFilter(request.GET, queryset=categories)
    categories = filters.qs

    context = {'categories': categories, 'filter': filters}
    template_name = 'admin-panel\category\index.html'
    return render(request, template_name, context)


@access_required
def show(request, id):
    #cat = Category.objects.get(id=id)
    #view = cat.view + 1
    #Category.objects.filter(id=id).update(view=view)
    category = Category.objects.filter(id=id)
    context = {'category': category}
    template_name = 'admin-panel\category\show.html'

    return render(request, template_name, context)


@access_required
def create(request):
    form = CategoryForm
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/category/')
        else:
            HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context = {'form': form}
    return render(request, "admin-panel\category\create_update.html", context)


@access_required
def update(request, id):
    category = Category.objects.get(id=id)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/category/')
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context = {'form': form}
    return render(request, 'admin-panel\category\\create_update.html', context)


@access_required
def delete(request, id):
    category = Category.objects.filter(id=id)
    category.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
