from django.shortcuts import render
from django.http import HttpResponse
from . import models

header = {'title': 'Интернет-магазин "Голубые гитары"', 'menu':[ {'name':'Главная', 'href':'index1'},
                                                                 {'name':'Каталог','href':'catalogue'},
                                                                 {'name':'Контакты', 'href':'contacts'} ]}

def index(request):
    user = request.user
    query = models.Product.objects.all()
    return render(request, 'products/index.html', {'query': query})


def index1(request):

    return render(request, 'products/index1.html', header)


def catalogue(request):

    return render(request, 'products/catalogue.html', header)


def contacts(request):

    return render(request, 'products/contacts.html', header)