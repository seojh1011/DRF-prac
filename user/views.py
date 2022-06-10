from urllib import response
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
    permission_classes = [VerifyPermissionLevel]
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        return Response({"message": "get success!"})

