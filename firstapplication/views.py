from django.shortcuts import render
from django.http import HttpResponse

from django.template import RequestContext


def index(request):
    #return HttpResponse("Hello, world. You're at the application index.")
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'firstapplication/index.html', context_dict)