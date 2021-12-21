from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') # CSDCASE: USER가 탈퇴하면 해당 PROFILE도 삭제된다

    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True) #unique=True면 유일한 닉네임을 가지도록 설정
    message = models.CharField(max_length=100, null=True)

