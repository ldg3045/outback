from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    # 토큰
    path("signin/", TokenObtainPairView.as_view(), name="token_obtain_pair"), # 로그인 / 엑세스 토큰 발급
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"), # 토큰 연장을 위한 리프레시 토큰 발급
    # 회원 기능
    path("signup/", views.SignupView.as_view(), name="signup"),
    path('<str:username>/', views.UserDetailView.as_view(), name='user_detail'),
]
