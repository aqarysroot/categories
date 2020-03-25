from rest_framework import viewsets
from .serializers import (
    CategorySerializer
)
from .models import Category
from django.views.generic import View
import requests
from django.http import HttpResponse
from django.template.response import TemplateResponse
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.root_nodes()
    serializer_class = CategorySerializer
    
def my_view(request):
    print('sss')
    # Create a response
    response = TemplateResponse(request, 'mytemplate.html', {})
    r = requests.get("https://order.al-style.kz/api/categories?access-token=46a9JxnqG5VW2dMb5aocd28NJstrz79z")

    # if Genre.objects.count() == 0:
    right = 0
    left = 0
    cat_l = []
    for categories in r.json():
        if categories['left'] > right :
            right = categories['right']
            left = categories['left']
            name1 = categories['name']
            c_id = categories['id']
            elements = categories['elements']
            cat_l = []
            p = Category.objects.create(name = name1, id=c_id,elements=elements)
            cat_l.append(p)
        else:
            if categories['right']-categories['left'] > 1:
                p = Category.objects.create(name=categories['name'], parent = cat_l[-1] , id=categories['id'],elements=categories['elements'])
                cat_l = cat_l[:categories['level']-1]

                cat_l.append(p)
            elif categories['right']-categories['left'] == 1:
                Category.objects.create(name=categories['name'], parent = cat_l[-1], id=categories['id'], elements=categories['elements'] )
    return response

def my_view2(request):
    print('sss')
    # Create a response
    response = TemplateResponse(request, 'mytemplate.html', {})
    r = requests.get("https://order.al-style.kz/api/categories?access-token=46a9JxnqG5VW2dMb5aocd28NJstrz79z")

    # if Genre.objects.count() == 0:
    right = 0
    left = 0
    cat_l = []
    for categories in r.json():
        if categories['left'] > right :
            right = categories['right']
            left = categories['left']
            name1 = categories['name']
            cat_l = []
            p = Category.objects.create(name = name1)
            cat_l.append(p)
        else:
            if categories['right']-categories['left'] > 1:
                p = Category.objects.create(name=categories['name'], parent = cat_l[-1] )
                cat_l = cat_l[:categories['level']-1]

                cat_l.append(p)
            elif categories['right']-categories['left'] == 1:
                Category.objects.create(name=categories['name'], parent = cat_l[-1] )
    return response


        