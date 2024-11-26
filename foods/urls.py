from django.urls import path
from .views import FoodTypeAPIView, FoodAPIView, CommentAPIView

urlpatterns = [
    path('food-types/', FoodTypeAPIView.as_view(), name='foodtype-list'),
    path('foods/', FoodAPIView.as_view(), name='food-list'),
    path('comments/', CommentAPIView.as_view(), name='comment-list'),
]

