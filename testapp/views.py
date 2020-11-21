from django.shortcuts import render
from .models import Post, Survey, UserInfo
from .serializers import PostSerializer, SurveySerializer, UserInfoSerializer, RecentPostSerializer
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by("-reg_dt")

    @action(methods=['post'])
    def write_post(self):
        serializer_class.save()



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
