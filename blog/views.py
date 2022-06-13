from datetime import timedelta,datetime

from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Article
from user.models import UserProfile


class WritePermissionLevel(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        result = bool(user.is_authenticated)
        return result


class BlogApiView(APIView):

    permission_classes = [WritePermissionLevel]

    def get(self, request):
        user = request.user
        profile = UserProfile.objects.filter(user=user)
        articles = Article.objects.filter(writer=user)
        if len(profile) == 0:
            profile = {'message':'프로필이 없습니다'}
        if len(articles) == 0:
            articles = {'message': '작성글이 없습니다'}
        ctx = [articles,profile]

        return Response(ctx)

    def post(self, request):

        user = request.user

        join_date = user.join_date.date()
        now = (datetime.now() - timedelta(days=3)).date()

        if join_date <= now:
            title = request.date.get('title','')
            category = request.date.get('category','')
            content = request.date.get('content','')
            new_aricle = Article.objects.create(title=title,category=category,content=content,writer=user)
            return Response(new_aricle)
        else:
            return Response({'error':'가입 3일후 작성 가능합니다.'})
