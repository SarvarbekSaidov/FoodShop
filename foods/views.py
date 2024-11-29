from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import FoodType, Food, Comment
from .serializers import FoodTypeSerializer, FoodSerializer, CommentSerializer
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAuthorOrReadOnly


class FoodTypeListView(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodListView(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class CommentAPIViewSet(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer