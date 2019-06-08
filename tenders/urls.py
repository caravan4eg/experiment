from django.urls import path
from .views import TenderAPIView


urlpatterns = [
                # path('viewset/', TenderViewSet.as_view()),
                path('<category_request>', TenderAPIView.as_view()),

            ]