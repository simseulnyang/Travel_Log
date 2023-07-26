from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'user'

urlpatterns = [

    # 회원가입
    path('register/', views.Registration.as_view(), name='register'),

    # 로그인
    path('login/', views.Login.as_view(), name='login'),

    # 로그아웃
    path('logout/', views.Logout.as_view(), name='logout'),

    # 프로필작성
    path('profile/edit/', views.ProfileWrite.as_view(), name="pf-write"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
