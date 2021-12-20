from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView, AccountDetailView

app_name = "accountapp"

# 127.0.0.1:8000/account/hello_world() -> 들어오고자 하는 함수, 하나씩 들어오기 힘들기 때문에 위와 같이 써둠

urlpatterns = [ # 해당 뷰 불러오기
    path('hello_world/', hello_world, name='hello_world'),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
]
