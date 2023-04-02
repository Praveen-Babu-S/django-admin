from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
# Create your views here.

def serveRoutes(request,month):
    if month == 'jan':
        return HttpResponse('This is Jan')
    elif month == 'feb':
        return HttpResponse('This is Feb')
    else:
        return HttpResponseNotFound('No route found')
