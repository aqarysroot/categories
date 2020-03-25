import requests
import json
from core.models import Category
from django.core.management.base import BaseCommand
from datetime import datetime


IMPORT_URL = 'https://order.al-style.kz/api/categories?access-token=46a9JxnqG5VW2dMb5aocd28NJstrz79z'

class Command(BaseCommand):
    def import_category(self, data):
        name = data.get('name', None)
        lft = data.get('left', None)
        rght = data.get('right', None)
        mptt_level = data.get('level', None)
        elements = data.get('elements', None)
        tree_id = data.get('id', None)
        id = data.get('id', None)
        
        try:
            
            category, created = Category.objects.get_or_create(
                name=name,
                lft=lft,
                rght=rght,
                mptt_level=mptt_level,
                elements=elements,
                tree_id = tree_id,
                id=id,
            )
            if created:
                category.save()
                display_format = "\Category, {}, has been saved."
                print(display_format.format(category))
        except Exception as ex:
            print(str(ex))
            msg = "\n\nSomething went wrong saving this Category: {}\n{}".format(name, str(ex))
            print(msg)


    def handle(self, *args, **options):
        """
        Makes a GET request to the  API.
        """
        headers = {'Content-Type': 'application/json'}
        response = requests.get(
            url=IMPORT_URL,
            headers=headers,
        )

        response.raise_for_status()
        data = response.json()

        for data_object in data:
            self.import_category(data_object)
            
            

    # for categories in r.json()[:5]:
    #     if categories['right'] - categories['left'] > 1:
    #           name1 = categories['name']
    #           p = Genre.objects.create(name = name1)
    #     else:
    #         Genre.objects.create(name=categories['name'], parent = p )