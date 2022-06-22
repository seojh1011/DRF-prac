from rest_framework import serializers
from user.models import User as UserModel
from user.models import UserProfile
from user.models import Hobby as HobbyModel

class HobbySerializer(serializers.ModelSerializer):
    # serializers.SerializerMethodField()를 사용해 원하는 필드를 생성한다.
    same_hobby_users = serializers.SerializerMethodField()
    def get_same_hobby_users(self, obj):
        user_list = []
        for user_profile in obj.userprofile_set.all():
            user_list.append(user_profile.user.username)

        return user_list

    class Meta:
        model = HobbyModel
        fields = ["name", "same_hobby_users"]

class UserProfileSerializer(serializers.ModelSerializer):
    # 외래 키 관계로 이어져 있는 필드는 Serializer를 바로 호출할 수 있다.
    hobby = HobbySerializer(many=True,required=False)

    class Meta:
        model = UserProfile
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    # One-to-one 관계에서는 fk처럼 사용 가능하다.
    # userprofile = UserProfileSerializer()

    class Meta:
        model = UserModel
        fields = ["username", "password", "fullname", "email"]
