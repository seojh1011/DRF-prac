from rest_framework import serializers

from blog.models import Article, Category
from user.serializer import UserSerializer


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"



class ArticleSerializer(serializers.ModelSerializer):

    article_category = CategorySerializer(many=True,required=False)
    writer = UserSerializer(required=False)
    get_article_categorys = serializers.ListField(required=False)
    class Meta:
        model = Article
        fields = "__all__"

    def create(self, validated_data):
        # print(validated_data.pop("get_article_categorys"))
        get_article_categorys =validated_data.pop("get_article_categorys")[0].split(",")
        article = Article(**validated_data)
        article.save()
        article.article_category.add(*get_article_categorys)
        return article