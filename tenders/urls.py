from django.urls import path
from .views import TenderAPIView, TenderCategoryAPIView


urlpatterns = [
                # path('viewset/', TenderViewSet.as_view()),
<<<<<<< HEAD
                path('<category_request>/', TenderAPIView.as_view()),
                path('category-list/<requested_category_list>', TenderCategoryAPIView.as_view()),
=======
                path('<category_request>', TenderAPIView.as_view()),
>>>>>>> 9f72dbb33a31da7fabee099fb0d2fbe64a398641

            ]