from rest_framework import routers
from .views import FoodTypeViewSet, FoodViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register('food-types', FoodTypeViewSet, basename='foodtype')
router.register('foods', FoodViewSet, basename='food')
router.register('comments', CommentViewSet, basename='comment')

urlpatterns = router.urls
