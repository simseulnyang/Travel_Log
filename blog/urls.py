from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # 글 목록
    path('', views.PostList.as_view(), name='list'),

    # 글 작성
    path('write/', views.PostWrite.as_view(), name='write'),

    # 글 상세페이지 조회
    path('detail/<int:pk>/', views.PostDetail.as_view(), name='detail'),

    # 글 수정
    path('detail/<int:pk>/edit/', views.PostUpdate.as_view(), name='edit'),

    # 글 삭제
    path('detail/<int:pk>/delete/', views.PostDelete.as_view(), name='delete'),
]
