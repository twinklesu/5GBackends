# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class UserInfo(models.Model):
    user_no = models.IntegerField(primary_key=True)
    user_id = models.CharField(max_length=200, blank=True, null=True)
    user_password = models.CharField(max_length=45, blank=True, null=True)
    user_name = models.CharField(max_length=45, blank=True, null=True)
    user_nicknm = models.CharField(max_length=45, blank=True, null=True)
    user_age = models.IntegerField(blank=True, null=True)
    user_sex = models.CharField(max_length=45, blank=True, null=True)
    user_tel = models.CharField(max_length=45, blank=True, null=True)
    user_address = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_info'


class Survey(models.Model):
    user_id = models.CharField(primary_key=True, max_length=200)
    reg_dt = models.DateTimeField()
    location = models.CharField(max_length=256, blank=True, null=True)
    weather = models.CharField(max_length=45, blank=True, null=True)
    fashion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey'
        unique_together = (('user_id', 'reg_dt'),)


class Post(models.Model):
    post_no = models.IntegerField(primary_key=True)
    post_title = models.CharField(max_length=128, blank=True, null=True)
    post_content = models.CharField(max_length=1028, blank=True, null=True)
    post_id = models.CharField(max_length=200, blank=True, null=True)
    reg_dt = models.DateTimeField(blank=True, null=True)
    mod_dt = models.DateTimeField(blank=True, null=True)
    post_image = models.TextField(blank=True, null=True)
    post_image_size = models.IntegerField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'post'
