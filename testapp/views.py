from django.shortcuts import render
from .models import Post, Survey, UserInfo, PostComment
from .serializers import PostSerializer, SurveySerializer, UserInfoSerializer, RecentPostSerializer, PostCommentSerializer, PasswordSerializer,
UserNicknameSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

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


#댓글 작성
class PostCommentViewSet(viewsets.ModelViewSet):
    serializer_class = PostCommentSerializer
    queryset = PostComment.objects.all()

# 댓글 받아오기
class GetPostCommentAPIView(APIView):
    def get(self, request, post_no):
        serializer = PostCommentSerializer(PostComment.objects.filter(post_no__exact=post_no), many=True)
        return Response(serializer.data)

# id 값으로 pw 리턴해서 프론트에서 매칭해서 맞는지 확인
class LoginAPIView(APIView):
    def get(self, request, user_id):
        serializer = PasswordSerializer(UserInfo.objects.filter(user_id = user_id), many=True)
        return Response(serializer.data)

# 게시글에서 id 검색으로 닉네임 리턴
class GetNicknameAPIView(APIView):
    def get(self, request, user_id):
        serializer = UserNicknameSerializer(UserInfo.objects.filter(user_id = user_id), many=True)
        return Response(serializer.data)

