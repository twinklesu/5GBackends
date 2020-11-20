from django.contrib import admin

# Register your models here.
#from .models import AuthUser
from .models import Post, Survey, UserInfo

#admin.site.register(AuthUser)
admin.site.register(Post)
admin.site.register(Survey)
admin.site.register(UserInfo)

