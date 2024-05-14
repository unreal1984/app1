from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
#    return HttpResponse('Home page')
    context = {
        'title': 'MY Home',
        'content': 'Main page - HOME',
        'list': ['1','2'],
        'dict': ['first', 1],
        'bool': True
    }
    return render(request, 'main/index.html', context)   

def about(request):
    return HttpResponse('about')