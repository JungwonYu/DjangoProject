from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(requset):
    return HttpResponse('하이요!') # 보여지는 내용 쓰기

