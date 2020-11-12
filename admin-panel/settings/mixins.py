from functools import wraps
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import Http404

def login_required(function):
    @wraps(function)
    def dispatch(request, *args, **kwargs):
        if request.user.is_authenticated:
            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/login/')
    return dispatch


def access_required(function):
    @wraps(function)
    def dispatch(request, *args, **kwargs):
        return function(request, *args, **kwargs)
    return dispatch
