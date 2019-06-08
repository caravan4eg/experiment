from .models import Tender, KeyWord
from .serializers import TenderSerializer

from rest_framework import generics

from datetime import date
from django.db.models import Q


# TODO поиск по любому слову вводится в форме на странице
# TODO вынести фильтр в отдельный файл
# + поиск по списку слов
# + выбор категории из GET запроса
# TODO add minus_keywords filter
# + выбор списка слов согласно категории
# + список слов из БД


class TenderAPIView(generics.ListAPIView):
    serializer_class = TenderSerializer
    name = 'All tenders list'

    def get_queryset(self):
        """
        This view should return a list of all tenders for
        category as determined by the category_request portion of the URL.
        category_list = (
                        'all',
                        'asutp',
                        'data centre', 
                        'lan',
                        'soft, hardware',
                        'ventilation',
                         )
        """
        wanted_items = set()
        category_request = self.kwargs['category_request']
        
        print('Request category - GET request: ', category_request)

        if category_request != 'all':
            obj = KeyWord.objects.get(category__startswith=category_request)
            plus_keywords = [word.strip() for word in obj.plus_keywords.split(',')]
            minus_keywords =[word.strip() for word in obj.minus_keywords.split(',')]
        else:
            return Tender.objects.all()  

        # filter qs by plus_keywords
        for word in plus_keywords:
            for item in Tender.objects.filter(
                                            Q(exp_date__gte=date.today()),
                                            Q(description__icontains=word),
                                            ):
                print('Search by word: ', word)
                print('----------------------------------------------\n')
                print(item.description)

                wanted_items.add(item.pk)

        # for word in minus_keywords:
        #     for item in wanted_items:
        #         if word in item:
        #             wanted_items.remove(item.pk)

        return Tender.objects.filter(pk__in=wanted_items)
 


