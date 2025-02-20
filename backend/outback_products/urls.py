from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Router는 ViewSet에 대한 URL을 자동으로 생성함.
router = DefaultRouter()
router.register('products', views.ProductViewSet) 
# 첫 번째 인자 'products'는 URL의 prefix가 됩니다
"""                              perfix란?

prefix는 URL의 앞부분, 즉 기본 경로를 의미

예시) prefix가 'products'이므로 모든 URL이 /products/로 시작하게 됩니다
- /products/ (목록)
- /products/1/ (상세)

"""
urlpatterns = [
    path('', include(router.urls)),
]
