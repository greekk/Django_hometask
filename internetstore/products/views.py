from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    user = request.user
    return render(request, 'products/index.html', {'data':{
                                                       'item1':{'name':'test item', 'image':'test image', 'cost': '1000'},
                                                       'item2':{'name':'test item2', 'image':'test image2', 'cost': '2000'},
                                                       'item3':{'name':'test item3', 'image':'test image3', 'cost': '3000'},
                                                       'item4':{'name':'test item4', 'image':'test image4', 'cost': '4000'}
                                                        }})