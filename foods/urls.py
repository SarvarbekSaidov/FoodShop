from django.urls import path
from .views import (
    FoodTypeListView, FoodTypeDetailView, FoodListView, FoodDetailView, CommentListView, CommentDetailView
)

urlpatterns = [
    path('food-types/', FoodTypeListView.as_view(), name='foodtype-list'),
    path('food-types/<int:pk>/', FoodTypeDetailView.as_view(), name='foodtype-detail'),
    path('foods/', FoodListView.as_view(), name='food-list'),
    path('foods/<int:pk>/', FoodDetailView.as_view(), name='food-detail'),
    path('comments/', CommentListView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]
