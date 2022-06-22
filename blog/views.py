from datetime import timedelta,datetime

from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Article
from blog.serializer import ArticleSerializer
from user.models import UserProfile, User
from user.serializer import UserSerializer


class WritePermissionLevel(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        result = bool(user.is_authenticated)
        return result


class BlogApiView(APIView):

    # permission_classes = [WritePermissionLevel]

    def get(self, request):
        user = request.user
        user_serializer = UserSerializer(user).data
        article_serializer = ArticleSerializer(user.article_set,many=True).data

        ctx = [user_serializer,article_serializer]

        return Response(ctx)

    def post(self, request):

        # join_date = user.join_date.date()
        # now = (datetime.now() - timedelta(days=0)).date()
        # user = request.user
        # title = request.data.get('title','')
        # article_category = request.data.get('article_category','')
        # content = request.data.get('content','')
        # print(category)
        # new_aricle = Article.objects.create(title=title,content=content,writer=user)
        # new_aricle.article_category.add(*article_category)
        # return Response('성공')

        user = request.user
        article_Serializer = ArticleSerializer(data=request.data)
        if article_Serializer.is_valid():
            article_Serializer.save(writer=user)
            return Response(article_Serializer.data, status=status.HTTP_200_OK)
        return Response(article_Serializer.errors, status=status.HTTP_400_BAD_REQUEST)

