from rest_framework import permissions

#  일반 유저는 GET 조회만 가능.  스태프는 POST, PUT, DELETE 가능
class IsAdminOrReadOnly(permissions.BasePermission):
    """  BasePermission : 커스텀 권한 클래스

    - BasePermission을 상속받아야 하는 이유:
    1. has_permission() 메서드를 오버라이드하기 위한 기본 구조 제공
    2. DRF의 권한 시스템과 호환되기 위한 기본 기능 제공
    3. 권한 검사 로직을 표준화된 방식으로 구현 가능

    - 읽기 작업(GET)은 모든 사용자에게 허용
    - 쓰기 작업(POST, PUT, DELETE)은 스태프 사용자에게만 허용
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True        # SAFE_METHODS = (GET, HEAD, OPTIONS)
#                               HEAD: GET과 비슷하지만 헤더 정보만 반환
#                               OPTIONS: API가 지원하는 메소드 정보를 조회
        return request.user and request.user.is_staff
#          현재 로그인한 └> 일반 유저             └> 스태프 권한 여부
                              