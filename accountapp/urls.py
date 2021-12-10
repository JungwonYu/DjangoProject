from django.urls import path

from accountapp.views import hello_world

app_name = "accountapp"

# 127.0.0.1:8000/account/hello_world() -> 들어오고자 하는 함수, 하나씩 들어오기 힘들기 때문에 위와 같이 써둠

urlpatterns = [
    path('hello_world/', hello_world, name = 'hello_world') #해당 뷰 불러오기
]