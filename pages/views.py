from django.shortcuts import HttpResponse
from django.template import loader

from .models import Visitor

def home(request):
    return HttpResponse('<h1>Hello there!</h1>')

def visitors(request):
    latest_visitors = Visitor.objects.all()
    template = loader.get_template('pages/index.html')
    context = { 'latest_visitor_list' : latest_visitors }
    return HttpResponse(template.render(context,request))