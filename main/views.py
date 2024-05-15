from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
#    return HttpResponse('Home page')
    context = {
        'title': 'Home - Main page',
        'content': 'Магазин мебели HOME',
        
    }
    return render(request, 'main/index.html', context)   

def about(request):
    context = {
        'title': 'Home - About',
        'content': 'About us',
        'text_on_page': 'Text  about us Text  about us Text  about us Text  about us Text  about us'
        
    }
    return render(request, 'main/about.html', context) 