from django.contrib import admin
from django.contrib.auth.models import Group

from user.models import User
from user.models import UserProfile
from user.models import Hobby


admin.site.unregister(Group)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username',)
    list_display_links = ('username',)

admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)
admin.site.register(Hobby)





