from .models import Tender, KeyWord
from .serializers import TenderSerializer

from rest_framework import generics

from datetime import date
from django.db.models import Q

# TODO поиск по любому слову вводится в форме на странице
# TODO поиск по списку слов
# TODO выбор категории из запроса
# TODO add minus_keywords filter
# + выбор списка слов согласно категории
# + список слов из БД


class TenderAPIView(generics.ListAPIView):
    serializer_class = TenderSerializer
    name = 'All tenders list'

    def get_queryset(self):

        # obj = KeyWord.objects.get(category__startswith='АСУТП')
        obj = KeyWord.objects.get(category__startswith='ЛВС')
        plus_keywords = [word.strip() for word in obj.plus_keywords.split(',')]
        minus_keywords =[word.strip() for word in obj.minus_keywords.split(',')]

        wanted_items = set()
        
        for word in plus_keywords:
            print('Word in plus_keywords: ', word)
        
            for item in Tender.objects.filter(
                                        Q(exp_date__gte=date.today()),
                                        Q(description__icontains=word)
                                            ):
                wanted_items.add(item.pk)
            
        return Tender.objects.filter(pk__in=wanted_items)
 


