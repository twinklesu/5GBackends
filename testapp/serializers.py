from rest_framework import serializers
from .models import Post, Survey, UserInfo, PostComment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('post_no','post_title', 'post_content', 'post_id','reg_dt', 'post_image',)

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('user_id', 'reg_dt', 'location','weather','fashion',)

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('user_no', 'user_id', 'user_password','user_name','user_nicknm','user_age','user_sex','user_tel','user_address',)

class RecentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('post_title', 'reg_dt',)

class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = ('post_no', 'user_id','reg_dt','comment',)

class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('user_password',)

class UserNicknameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('user_nicknm',)
