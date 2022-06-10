
from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField("사용자 계정", max_length=20, unique= True)
    email = models.EmailField("이메일 주소", max_length= 40, unique= True)
    password = models.CharField("비밀 번호", max_length= 20)
    fullname = models.CharField("이름", max_length= 20)
    join_date = models.DateTimeField("가입일", auto_now_add= True)

    def __str__(self):
        return f"사용자이름: {self.username} 이메일: {self.email}"

class UserProfile(models.Model):
    user = models.OneToOneField(to= User, verbose_name= "사용자", on_delete=models.CASCADE)
    hobby = models.ManyToManyField(to="Hobby", verbose_name="취미")
    introduction = models.TextField("소개")
    birthday = models.DateField("생일")
    age = models.IntegerField("나이")

class Hobby(models.Model):
    name = models.CharField("취미", max_length=30)