from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from .models import Tender
from django_filters import CharFilter, BaseInFilter
from django.db import models



class SomewordsFilter(BaseInFilter, CharFilter):
    pass


class SearchFilter(FilterSet):
    # multiple search doesn't work
    # description_contains = SomewordsFilter(field_name='description', 
                                        #    lookup_expr='icontains')
    
    # single search works
    description_contains = CharFilter(field_name='description', 
                                           lookup_expr='icontains')

    class Meta:

        filter_overrides = {
             models.CharField: {
                 'filter_class': CharFilter,
                 'extra': lambda f: {
                     'lookup_expr': 'icontains',
                 },
             },
        }


