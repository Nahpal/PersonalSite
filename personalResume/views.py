from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader

def index(request):
    document = (loader.get_template('index.html')).render({})

    return HttpResponse(document)
