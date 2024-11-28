from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import FoodType, Food, Comment
from .serializers import FoodTypeSerializer, FoodSerializer, CommentSerializer

class FoodTypeListView(generics.ListCreateAPIView):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer


class FoodTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer

class FoodListView(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
<<<<<<< Updated upstream
=======
    permission_classes = [IsAuthorOrReadOnly]
>>>>>>> Stashed changes

class CommentListView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
