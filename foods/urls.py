from rest_framework import routers
from .views import FoodTypeListView, FoodListView, CommentAPIViewSet

router = routers.DefaultRouter()
router.register('food-types', FoodTypeListView, basename='foodtype')
router.register('foods', FoodListView, basename='food')
router.register('comments', CommentAPIViewSet, basename='comment')

urlpatterns = router.urls
