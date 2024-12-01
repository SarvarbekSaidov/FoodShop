from rest_framework.viewsets import ModelViewSet
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from django.core.mail import send_mail
from .models import FoodType, Food, Comment
from .serializers import FoodTypeSerializer, FoodSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly


class FoodTypeViewSet(ModelViewSet):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle]   

    def perform_create(self, serializer):
        instance = serializer.save()
        send_mail(
            subject="New Food Type Created",
            message=f"A new food type '{instance.name}' has been added.",
            from_email="saidovsarvarbek01@gmail.com",
            recipient_list=["saidovsarvarbek02@gmail.com"],
            fail_silently=False,
        )


class FoodViewSet(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle]   

    def perform_create(self, serializer):
        instance = serializer.save()
        send_mail(
            subject="New Food Created",
            message=f"A new food '{instance.name}' has been added.",
            from_email="saidovsarvarbek01@gmail.com",
            recipient_list=["saidovsarvarbek02@gmail.com"],
            fail_silently=False,
        )


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]  
    throttle_classes = [UserRateThrottle, AnonRateThrottle]   

    def perform_create(self, serializer):
        instance = serializer.save()
        send_mail(
            subject="New Comment Added",
            message=f"A new comment '{instance.content}' has been added by {instance.author}.",
            from_email="saidovsarvarbek01@gmail.com",
            recipient_list=["saidovsarvarbek02@gmail.com"],
            fail_silently=False,
        )
