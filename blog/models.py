from django.db import models
from user.models import User
# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=30,verbose_name='카테고리')
    description = models.CharField(max_length=200,verbose_name='설명')


class Article(models.Model):
    writer = models.ForeignKey(User,max_length=30,verbose_name='작성자', on_delete=models.CASCADE)
    title = models.CharField(max_length=100,verbose_name='제목')
    content = models.CharField(max_length=200, verbose_name='내용')
    article_category = models.ManyToManyField(Category,verbose_name='카테고리')
