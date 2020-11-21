from django.shortcuts import render
from .models import Post, Survey, UserInfo
from .serializers import PostSerializer, SurveySerializer, UserInfoSerializer, RecentPostSerializer
from rest_framework import viewsets, permissions

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.Post.objects.all().order_by("-reg_dt")



class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

# order by practice
class RecentPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by("-reg_dt")[:5]
    serializer_class = RecentPostSerializer
