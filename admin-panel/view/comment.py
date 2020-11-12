from django.shortcuts import render, HttpResponseRedirect
from ..models import Comment
from ..settings.mixins import login_required, access_required


@access_required
def index(request):
    comments = Comment.objects.all()
    context = {'comments': comments}
    return render(request, 'admin-panel\comment\index.html', context)


@access_required
def show(request, id):
    comment = Comment.objects.get(id=id)
    context = {'comment': comment}
    return render(request, 'admin-panel\comment\show.html', context)


@access_required
def status(request, id):
    comment = Comment.objects.get(id=id)
    if comment.status == 'e':
        comment.status = 'd'
    elif comment.status == 'd':
        comment.status = 'e'
    comment.save()
    return HttpResponseRedirect('/comment/')


@access_required
def delete(request, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return HttpResponseRedirect('/comment/')

