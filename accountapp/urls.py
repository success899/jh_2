from django.urls import path
from rest_framework.authtoken import views

from accountapp.views import hello_world, hello_world_template, AccountCreateTemplate, AccountCreateAPIView, ListUsers

app_name = 'accountapp'

urlpatterns = [
    # UI를 보기 위한 부분
    path('hello_world_template/', hello_world_template, name='hello_world_template'),
    # 로직 처리 위한 부분
    path('hello_world/', hello_world, name='hello_world'),

    # 토큰을 가져오기 위한 부분
    path('login/', views.obtain_auth_token, name='login'),

    # 유저 전체 리스트를 확인하는 부분
    path('list/', ListUsers.as_view(), name='list'),

    path('create_template/', AccountCreateTemplate, name='create_template'),
    path('create/', AccountCreateAPIView.as_view(), name='create'),
]