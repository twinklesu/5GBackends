from rest_framework import serializers
from .models import Post, UserInfo, PostComment, SurveyF, SurveyW

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('post_no','post_title', 'post_content', 'post_id','reg_dt', 'post_image',)

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('user_id', 'user_password', 'user_name','user_sex','user_tel',)

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

class UserLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('user_id','likes',)

class SurveyFSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyF
        fields = ('user_id', 'reg_dt', 'fashion')

class SurveyWSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyW
        fields = ('user_id', 'reg_dt', 'weather')

