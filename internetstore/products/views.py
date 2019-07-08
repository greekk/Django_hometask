from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from . import models



# def index2(request):
#     user = request.user
#     query = models.Product.objects.all()
#     return render(request, 'products/index2.html', {'query': query})

content = """Интернет-магазин "Голубые гитары" приветствует начинающих и профессиональных гитаристов!!<br>
                У нас вы найдете гитары на любой вкус и цвет. <br>
                Различных форм и содержания. <br>
                Для разнообразных направлений и стилей музыки"""
title = 'Интернет-магазин "Голубые гитары"'
menu = [{'name':'Главная', 'href':'main'}, {'name':'Каталог','href':'catalogue'}, {'name':'Контакты', 'href':'contacts'}]
copyright = '&copy; Все права защищены'

def main(request):

    return render(request, 'products/index.html', {'title':title, 'menu':menu, 'copyright':copyright, 'content':content})


def catalogue(request):

    query = get_list_or_404(models.Product)

    return render(request, 'products/catalogue.html', {'title':title, 'menu':menu, 'copyright':copyright, 'query': query})


def contacts(request):

    return render(request, 'products/contacts.html', {'title':title, 'menu':menu, 'copyright':copyright})


def details(request, pk):

    product = get_object_or_404(models.Product, id=pk)

    return render(request, 'products/detail.html', {'title':title, 'menu':menu, 'copyright':copyright, 'product':product})