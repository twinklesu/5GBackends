from django.shortcuts import render
from .models import Post, Survey, UserInfo, PostComment
from .serializers import PostSerializer, SurveySerializer, UserInfoSerializer, RecentPostSerializer, PostCommentSerializer, PasswordSerializer, UserNicknameSerializer
from .serializers import UserLikesSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404


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

# 회원가입
class JoinViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

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

# 등록되어 있는 id 이면 False 리턴
class ValidateIdAPIView(APIView):
    def get(self, request, user_id):
        if UserInfo.objects.filter(user_id = user_id).exists():
            return Response(data={'message':False}) #이 id 이미 있다
        else:
            return Response(data={'message':True})

# 등록되어 있는 id 이면 False 리턴
class ValidateNicknameAPIView(APIView):
    def get(self, request, user_nicknm):
        if UserInfo.objects.filter(user_nicknm = user_nicknm).exists():
            return Response(data={'message':False}) #이 닉네임 이미 있다
        else:
            return Response(data={'message':True})

# ootd 게시글에서 좋아요 누르면 user likes +1
class OotdLikesAPIView(APIView):
    def get(self, request, user_id):
        serializer = UserLikesSerializer(UserInfo.objects.filter(user_id = user_id), many=True)
        return Response(serializer.data)

    def get_object(self, user_id):
        try:
            return UserInfo.objects.get(user_id = user_id)
        except UserInfo.DoesNotExist:
            raise Http404

    def put(self, request, user_id, format=None):
        _user_id = self.get_object(user_id)
        serializer = UserLikesSerializer(_user_id, data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

#댓글 작성
class OotdLikesViewSet(viewsets.ModelViewSet):
    serializer_class = UserLikesSerializer
    queryset = UserInfo.objects.get(user_id = request.data)