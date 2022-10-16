from django.contrib import admin
from django.urls import path, include
from appTest import views #views.py 함수 쓰기 위한 import

urlpatterns = [
    #사용자가 admin이 아닌 다른 경로로 접속하면
    path('', views.index), #path가 없는 경로로 들어올 때, views의 index가 실행될 것이다.
    path('create/', views.create), #사용자가 create를 들어왔을 때
    path('read/<id>/', views.read),
    path('delete/', views.delete),
    path('update/<id>/', views.update)
]
#각각의 경로로 접속했을 때 views로 전달하려면?
