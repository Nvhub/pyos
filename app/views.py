from django.shortcuts import render, HttpResponse


def page404(request, exception):
    data = {}
    return render(request, 'more\\404.html', data)