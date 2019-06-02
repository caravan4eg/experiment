from django.urls import path
from .views import TenderAPIView


urlpatterns = [
                # path('viewset/', TenderViewSet.as_view()),
                path('', TenderAPIView.as_view()),

            ]