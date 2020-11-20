from django.shortcuts import render
from .models import Post, Survey, UserInfo
from .serializers import PostSerializer, SurveySerializer, UserInfoSerializer
from rest_framework import viewsets, permissions

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #permission_classes = [permissions.IsAuthenticated]

class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

# modification from window
# modification from ubuntu
