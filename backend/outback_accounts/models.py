from datetime import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):

    password = models.CharField(max_length=30) # ┌> 같은 이름 중복 방지
    username = models.CharField(max_length=30, unique=True, primary_key=True)
    """                     AbstractUser 모델에서 PK 설정시 설명 <┘
    JWT 토큰은 기본적으로 User 모델의 'id' 필드를 사용하려고 하는데,
    primary_key를 username으로 설정해서 id 필드가 없어진 것이 문제다.

    settings.py에 가서 아래에 JWT 설정을 추가해준다.

# ┌ JWT 설정
    SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
# └ 까지가 기존 코드
    # 아래 두 줄 추가
    "USER_ID_FIELD": "username",  # User 모델의 프라이머리 키 필드
    "USER_ID_CLAIM": "username",  # 토큰에 저장될 사용자 식별자
    
    """
    email = models.EmailField(blank=True)
    user_bio = models.TextField(max_length=150, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True) # 생성 날짜

    def __str__(self):
        return self.username


"""이전 코드
class User(AbstractUser):
    pass
"""