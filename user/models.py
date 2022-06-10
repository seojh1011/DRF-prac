from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField("사용자 계정", max_length=20, unique=True)
    email = models.EmailField("이메일 주소", max_length=100, unique=True)
    password = models.CharField("비밀번호", max_length=300)
    join_date = models.DateTimeField("가입일", auto_now_add=True)
    permission_level = models.IntegerField(default=0)
    
    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(to=User, verbose_name="사용자", on_delete=models.CASCADE, primary_key=True)
    server = models.ManyToManyField(to="Server", verbose_name="서버")
    nationality = models.ManyToManyField(to="Nationality", verbose_name="국적")
    introduction = models.TextField("소개")
    
    def __str__(self):
        return f'{self.user.username}님의 인게임 프로필입니다'


class Server(models.Model):
    name = models.CharField("서버", max_length=10)
    
    def __str__(self) -> str:
        return self.name
    
    
class Nationality(models.Model):
    name = models.CharField("국적", max_length=10)
    
    def __str__(self) -> str:
        return self.name