from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import FoodTypeViewSet, FoodViewSet, CommentViewSet

router = DefaultRouter()
router.register('food-types', FoodTypeViewSet, basename='foodtype')
router.register('foods', FoodViewSet, basename='food')
router.register('comments', CommentViewSet, basename='comment')

urlpatterns = router.urls
