from rest_framework import serializers
from .models import User
from django.core.exceptions import ValidationError

#"""이전 코드
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = "__all__"

    def validate_Userpassword(self, password):
        # 비밀번호에 문자 포함 검사
        if not any(char.isalpha() for char in password):
            raise ValidationError("비밀번호에 문자는 필수입니다.")
        # 비밀번호에 숫자 포함 검사
        if not any(char.isdigit() for char in password):
            raise ValidationError("비밀번호에 숫자는 필수입니다.")
        return password

    def validate_check(self, data):
        # 비밀번호 일치 여부 검사
        if data['password'] != data['password2']:
            raise ValidationError("비밀번호가 일치하지 않습니다.")
        return data

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
            
        )
        return user
#"""


