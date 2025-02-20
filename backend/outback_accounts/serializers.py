from time import localtime
from rest_framework import serializers
from .models import User
from django.core.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    # 비밀번호, 비밀번호 확인 
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True, required=True)
    # 가입 날짜 포맷 커스터마이징
    date_joined = serializers.DateTimeField(format="%Y-%m-%d", required=False)
    #                                   가입 할 때, 날짜 입력 안 해도 됨<┘


    class Meta:
        model = User
        exclude = (         # 제외할 필드들
            'is_superuser',
            'first_name',
            'last_name',
            'is_staff',
            'is_active',
            'groups',
            'user_permissions',
            'last_login',

        )
        extra_kwargs = {  # 필드에 대한 추가 설정을 제공
            'username': {'required': True,             # username 필드는 필수
            'help_text': '사용자 이름을 입력하세요'},  # 필드 설명 추가
            'password': {'write_only': True},  
        }            #     └> True로 설정하면 해당 필드는 쓰기만 가능 (API 응답에서는 보이지 않음)
    
    # 마지막 로그인 시간
    def get_last_login(self, obj):
        if obj.last_login:
            return localtime(obj.last_login).strftime("%Y-%m-%d")
        return None        

    # 비밀번호 조건 유효성 검사
    def validate_Userpassword(self, password):
        # 비밀번호에 문자 포함 검사
        if not any(char.isalpha() for char in password):
            raise ValidationError("비밀번호에 문자는 필수입니다.")
        # 비밀번호에 숫자 포함 검사
        if not any(char.isdigit() for char in password):
            raise ValidationError("비밀번호에 숫자는 필수입니다.")
        return password

    # 비밀번호 일치 검사
    def validate_check(self, data):
        # 비밀번호 일치 여부 검사
        if data['password'] != data['password2']:
            raise ValidationError("비밀번호가 일치하지 않습니다.")
        return data

    # 비밀번호 생성
    def create(self, validated_data):
        # password 유효성 검사
        self.validate_Userpassword(validated_data['password'])
        # 비밀번호 일치 검사
        self.validate_check(validated_data)
        
        # password2 필드 제거 (User 모델에 없는 필드)
        validated_data.pop('password2')
        
        # create_user 메서드로 유저 생성 (비밀번호 해싱 포함)
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            user_bio=validated_data.get('user_bio', ''),

        )
        return user



