from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('news_list/', views.news_list, name='news_list'),                   #뉴스 리스트
    path('news_content/<int:news_id>', views.news_content, name='news_content'),                  #뉴스 내용
]