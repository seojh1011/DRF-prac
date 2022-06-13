from urllib import response

from django.contrib.auth import authenticate, login
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import permissions


class VerifyPermissionLevel(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        result = bool(user and user.is_authenticated and user.permission_level >= 0)
        return result


class UserApiView(APIView):
    # permission_classes = [VerifyPermissionLevel]
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        return Response({"message": "get success!"})

    def post(self, request):
        username = request.data.get('username','')
        password = request.data.get('password','')
        user = authenticate(request, username=username, password=password)

        if not user:
            return Response({'error':'아이디 또는 비밀번호 오류입니다'})

        login(request, user)
        return Response({'message':'로그인 성공'})

