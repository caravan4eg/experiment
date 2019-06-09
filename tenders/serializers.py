from rest_framework import serializers  
from .models import Tender, KeyWord


class TenderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tender
        fields = '__all__'


class TenderCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = KeyWord
        fields = '__all__'
