from django.shortcuts import render
from .models import Post, Survey, UserInfo, PostComment
from .serializers import PostSerializer, SurveySerializer, UserInfoSerializer, RecentPostSerializer, PostCommentSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by("-reg_dt")

class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

class RecentPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by("-reg_dt")[:5]
    serializer_class = RecentPostSerializer

class PostCommentViewSet(viewsets.ModelViewSet):
    serializer_class = PostCommentSerializer
    def post_comment(self, request):
        post_id = int(request.GET['post_no'])
        queryset = PostComment.objects.filter(post_no__exact=post_id)
        return Response(queryset)

