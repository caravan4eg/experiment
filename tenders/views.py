from .models import Tender
from .serializers import TenderSerializer

from rest_framework import generics

from datetime import date
from django.db.models import Q


class TenderAPIView(generics.ListAPIView):
    serializer_class = TenderSerializer
    name = 'All tenders list'

    def get_queryset(self):
        plus_words = ['сети', 'данных']
        wanted_items = set()

        for word in plus_words:
        
            for item in Tender.objects.filter(Q(exp_date__gte=date.today()),Q(description__icontains=word)):
                wanted_items.add(item.pk)
            
        return Tender.objects.filter(pk__in=wanted_items)
 


