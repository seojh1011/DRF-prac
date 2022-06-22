
from django.contrib.auth import authenticate, login


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from user.models import User
from user.serializer import UserSerializer

class VerifyPermissionLevel(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        result = bool(user and user.is_authenticated and user.permission_level >= 0)
        return result


class UserApiView(APIView):
    # permission_classes = [VerifyPermissionLevel]
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request):

        user_serializer = UserSerializer(User.objects.all(),many=True).data

        return Response(user_serializer, status=status.HTTP_200_OK)

    def post(self, request):

        # user_serializer = UserSerializer(data=request.data)
        #
        # if user_serializer.is_valid():
        #     user_serializer.save()
        #     return Response(user_serializer.data, status=status.HTTP_200_OK)
        #
        # return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        username = request.data.get('username','')
        password = request.data.get('password','')
        user = authenticate(request, username=username, password=password)

        if not user:
            return Response({'error':'아이디 또는 비밀번호 오류입니다'})

        login(request, user)
        return Response({'message':'로그인 성공'})

