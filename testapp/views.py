from django.shortcuts import render
from .models import Post, UserInfo, PostComment, SurveyF, SurveyW
from .serializers import PostSerializer, RecentPostSerializer, PostCommentSerializer, PasswordSerializer, UserNicknameSerializer
from .serializers import UserLikesSerializer, UserInfoSerializer, SurveyFSerializer, SurveyWSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404, HttpResponse
from django.db import connection

class PostViewSet(APIView):
    def get(self, request):
        serializer = PostSerializer(Post.objects.all().order_by("-reg_dt"))
        return Response(data = serializer.data)

class RecentPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by("-reg_dt")[:5]
    serializer_class = RecentPostSerializer

# 회원가입
class JoinViewSet(viewsets.ModelViewSet):
    serializer_class = UserInfoSerializer
    queryset = UserInfo.objects.all()


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
        serializer = UserLikesSerializer(_user_id, data = request.user.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

#댓글 작성
class OotdLikesViewSet(viewsets.ModelViewSet):
    def update(self, request, user_id=None):
        user_id = request.user.user_id
        queryset = UserInfo.objects.filter(user_id=user_id)
        if not queryset:
            return
        else:
            serializer = UserLikesSerializer(queryset)
            serializer.save()
            return Response(serializer.data)

# 날씨 설문
class WeatherSurveyViewSet(viewsets.ModelViewSet):
    serializer_class = SurveyWSerializer
    queryset = SurveyW.objects.all()

# 패션설문
class FashionSurveyViewSet(viewsets.ModelViewSet):
    serializer_class = SurveyFSerializer
    queryset = SurveyF.objects.all()

class WeatherResultAPIView(APIView):
    def get(self, request):
        try:
            cursor = connection.cursor()
            strSql = "select weather from survey_w where time_to_sec(timediff(now(), reg_dt)) < 21600 group by weather order by count(*) desc limit 2;"
            result = cursor.execute(strSql)
            weather = cursor.fetchall()
            connection.commit()
            connection.close()
        except:
            connection.rollback()
        return Response(data={'weather': weather})

class FashionResultAPIView(APIView):
    def get(self, request):
        try:
            cursor = connection.cursor()
            strSql = "select fashion from survey_f where time_to_sec(timediff(now(), reg_dt)) < 21600 group by fashion order by count(*) desc limit 4;"
            result = cursor.execute(strSql)
            fashion = cursor.fetchall()
            connection.commit()
            connection.close()
        except:
            connection.rollback()
        return Response(data={'fashion': fashion})
