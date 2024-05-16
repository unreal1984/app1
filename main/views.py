#from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

# Create your views here.
def index(request):
    
    
    categories = Categories.objects.all()
#    return HttpResponse('Home page')
    context = {
        'title': 'Home - Main page',
        'content': 'Магазин мебели HOME',
        'categories': categories
        
    }
    return render(request, 'main/index.html', context)   

def about(request):
    context = {
        'title': 'Home - About',
        'content': 'About us',
        'text_on_page': 'Text  about us Text  about us Text  about us Text  about us Text  about us'
        
    }
    return render(request, 'main/about.html', context) 