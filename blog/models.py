from django.db import models
from user.models import User
# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=30,verbose_name='카테고리')
    description = models.CharField(max_length=200,verbose_name='설명')

    def __str__(self):
        return self.category


class Article(models.Model):
    writer = models.ForeignKey(User,max_length=30,verbose_name='아티클작성자', on_delete=models.CASCADE)
    title = models.CharField(max_length=100,verbose_name='제목')
    content = models.CharField(max_length=200, verbose_name='내용')
    article_category = models.ManyToManyField(Category,verbose_name='카테고리')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, verbose_name='게시글',on_delete=models.CASCADE)
    writer = models.ForeignKey(User,verbose_name='코멘트작성자',on_delete=models.CASCADE)
    comment = models.CharField(max_length=200,verbose_name='코멘트내용')
    created_at = models.DateTimeField(auto_now_add=True)