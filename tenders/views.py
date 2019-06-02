from .models import Tender
from .serializers import TenderSerializer

# from rest_framework import viewsets
from rest_framework import generics


# class TenderViewSet(viewsets.ModelViewSet):
#     queryset = Tender.objects.all()
#     serializer_class = TenderSerializer


class TenderAPIView(generics.ListAPIView):
    serializer_class = TenderSerializer
    queryset = Tender.objects.all()
    name = 'All tenders list'

