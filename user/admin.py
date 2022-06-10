from django.contrib import admin
from django.contrib.auth.models import Group

from user.models import User as UserModel
from user.models import UserProfile
from user.models import Server as ServerModel
from user.models import Nationality as NationalityModel


admin.site.unregister(Group)

class idcheck(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(UserModel)
admin.site.register(UserProfile)
admin.site.register(ServerModel, idcheck)
admin.site.register(NationalityModel, idcheck)





