from .models import Tender
from .serializers import TenderSerializer

from rest_framework import generics


class TenderAPIView(generics.ListAPIView):
    serializer_class = TenderSerializer
    queryset = Tender.objects.all()
    name = 'All tenders list'

