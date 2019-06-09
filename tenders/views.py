from .models import Tender, KeyWord
from .serializers import TenderSerializer, TenderCategorySerializer

from rest_framework import generics

from datetime import date
from django.db.models import Q

import django.http.request


# TODO поиск по любому слову вводится в форме на странице
# TODO вынести фильтр в отдельный файл
# TODO add minus_keywords filter
# + ввод и фильтр по нескольким категориям
# + выбор списка слов согласно категории
# + список слов из БД
# + поиск по списку слов
# + выбор категории из GET запроса


class TenderCategoryAPIView(generics.ListAPIView):
    serializer_class = TenderCategorySerializer
    name = "All category list"

    def get_queryset(self):
        """
        This view should return a list of all tenders category for
        categories and related keywords  as determined 
        by the tender category_request portion of the URL.
        """
        wanted_category = set()

        category_list = (
                        'all',
                        'asutp',
                        'data centre', 
                        'lan',
                        'soft, hardware',
                        'ventilation',
                         )
        # getting categories from GET request
        requested_categories = [
                    category.strip() for category in category_list 
                    if category in self.kwargs['requested_category_list']
                    ]
        print('REQUESTED LIST CATEGORIES: ', requested_categories)
        
        # getting queryset for choosen categories
        if 'all' in requested_categories:
            return KeyWord.objects.all()
        
        for category in requested_categories:
            item = KeyWord.objects.get(category__startswith=category)
            wanted_category.add(item.pk)
            
        return KeyWord.objects.filter(pk__in=wanted_category)
        
        

class TenderAPIView(generics.ListAPIView):
    serializer_class = TenderSerializer
    name = 'All tenders list'

    def get_queryset(self):
        """
        This view should return a list of all tenders for
        category as determined by the 
        category_request portion of the URL.
        """
        
        wanted_items = set()
        category_list = (
                        'all',
                        'asutp',
                        'data centre', 
                        'lan',
                        'soft, hardware',
                        'ventilation',
                         )

        # get list requested categories from GET request
        # and check if they are in category_list
        requested_categories = [
                                category.strip() for category in category_list 
                                if category in self.kwargs['category_request']
                                ]
                
        if 'all' in requested_categories:
            print('Requested CATEGORIES: ', requested_categories)

            return Tender.objects.all()
        
        for category in requested_categories:
            print('Requested CATEGORY: ', category)
            obj = KeyWord.objects.get(category__startswith=category)
            plus_keywords = [word.strip() for word in obj.plus_keywords.split(',')]
            minus_keywords =[word.strip() for word in obj.minus_keywords.split(',')]
            
            
        # filter by plus_keywords
            for word in plus_keywords:
                for item in Tender.objects.filter(
                                                Q(exp_date__gte=date.today()),
                                                Q(description__icontains=word),
                                                ):
                    print('----------------------------------------------')
                    print('Tender filtered by word: ', word)
                    print(f'Number: {item.number} \nDescription: {item.description}\n')
                    print('----------------------------------------------\n')
                    
                    wanted_items.add(item.pk)

        # for word in minus_keywords:
        #     for item in wanted_items:
        #         if word in item:
        #             wanted_items.remove(item.pk)

        return Tender.objects.filter(pk__in=wanted_items)
 


