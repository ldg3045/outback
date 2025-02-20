import requests
import streamlit as st

# 웹 애플리케이션 제목 설정
st.title("Django API 연동 예제")

# 로그인 세션 관리를 위한 상태 초기화
if 'access_token' not in st.session_state:
    st.session_state.access_token = None  # JWT 토큰 저장용
if 'username' not in st.session_state:
    st.session_state.username = None  # 사용자 이름 저장용

# 로그인 상태에 따른 사이드바 메뉴 표시
if st.session_state.access_token:  # 로그인된 경우
    menu = st.sidebar.selectbox(
        "메뉴를 선택하세요",
        ["회원정보 조회", "회원정보 수정", "회원 탈퇴", "로그아웃"],
        key="logged_in_menu"
    )
else:  # 로그인되지 않은 경우
    menu = st.sidebar.selectbox(
        "메뉴를 선택하세요",
        ["로그인", "회원가입"],
        key="logged_out_menu"
    )

# 로그인 페이지
if menu == "로그인":
    st.header("로그인")
    username = st.text_input("Username")  # 사용자 이름 입력
    password = st.text_input("Password", type="password")  # 비밀번호 입력 (마스킹 처리)
    
    if st.button("로그인"):  # 로그인 버튼 클릭 시
        # Django 서버로 로그인 요청 전송
        response = requests.post(
            "http://127.0.0.1:8000/api/v1/outback_accounts/signin/",
            json={"username": username, "password": password}
        )
        if response.status_code == 200:  # 로그인 성공
            data = response.json()
            st.session_state.access_token = data['access']  # JWT 토큰 저장
            st.session_state.username = username  # 사용자 이름 저장
            st.success("로그인 성공!")
            st.rerun()  # 페이지 새로고침
        else:  # 로그인 실패
            st.error("로그인 실패")

# 회원가입 페이지
elif menu == "회원가입":
    st.header("회원가입")
    username = st.text_input("Username")  # 사용자 이름 입력
    password = st.text_input("Password", type="password")  # 비밀번호 입력
    password2 = st.text_input("Password Confirm", type="password")  # 비밀번호 확인
    email = st.text_input("Email")  # 이메일 입력
    user_bio = st.text_area("User_Bio")  # 자기소개 입력
    
    if st.button("회원가입"):  # 회원가입 버튼 클릭 시
        try:
            # Django 서버로 회원가입 요청 전송
            response = requests.post(
                "http://127.0.0.1:8000/api/v1/outback_accounts/signup/",
                json={
                    "username": username,
                    "password": password,
                    "password2": password2,
                    "email": email,
                    "user_bio": user_bio
                }
            )
            if response.status_code == 201:  # 회원가입 성공
                st.success("회원가입 성공!")
            else:  # 회원가입 실패
                error_msg = response.json() if response.text else "회원가입 실패"
                st.error(f"회원가입 실패: {error_msg}")
        except Exception as e:  # 예외 발생 시
            st.error(f"요청 실패: {str(e)}")

# 로그아웃 처리
elif menu == "로그아웃":
    st.session_state.access_token = None  # JWT 토큰 제거
    st.session_state.username = None  # 사용자 이름 제거
    st.success("로그아웃 되었습니다.")
    st.rerun()  # 페이지 새로고침

# 회원정보 조회 페이지
elif menu == "회원정보 조회":
    st.header("회원정보 조회")
    # JWT 토큰을 헤더에 포함
    headers = {"Authorization": f"Bearer {st.session_state.access_token}"}
    # Django 서버로 회원정보 조회 요청 전송
    response = requests.get(
        f"http://127.0.0.1:8000/api/v1/outback_accounts/{st.session_state.username}/",
        headers=headers
    )
    if response.status_code == 200:  # 조회 성공
        st.json(response.json())  # JSON 형태로 회원정보 표시
    else:  # 조회 실패
        st.error("조회 실패")

# 회원정보 수정 페이지
elif menu == "회원정보 수정":
    st.header("회원정보 수정")
    user_bio = st.text_area("New Bio")  # 새로운 자기소개 입력
    
    if st.button("수정"):  # 수정 버튼 클릭 시
        # JWT 토큰을 헤더에 포함
        headers = {"Authorization": f"Bearer {st.session_state.access_token}"}
        # Django 서버로 회원정보 수정 요청 전송
        response = requests.put(
            f"http://127.0.0.1:8000/api/v1/outback_accounts/{st.session_state.username}/",
            headers=headers,
            json={"user_bio": user_bio}
        )
        if response.status_code == 200:  # 수정 성공
            st.success("수정 성공!")
            st.json(response.json())  # 수정된 정보 표시
        else:  # 수정 실패
            st.error(f"수정 실패: {response.text}")

# 회원 탈퇴 페이지
elif menu == "회원 탈퇴":
    st.header("회원 탈퇴")
    if st.checkbox("정말 탈퇴하시겠습니까?"):  # 확인 체크박스
        if st.button("탈퇴"):  # 탈퇴 버튼 클릭 시
            # JWT 토큰을 헤더에 포함
            headers = {"Authorization": f"Bearer {st.session_state.access_token}"}
            # Django 서버로 회원 탈퇴 요청 전송
            response = requests.delete(
                f"http://127.0.0.1:8000/api/v1/outback_accounts/{st.session_state.username}/",
                headers=headers
            )
            if response.status_code == 204:  # 탈퇴 성공
                st.session_state.access_token = None  # JWT 토큰 제거
                st.session_state.username = None  # 사용자 이름 제거
                st.success("탈퇴 완료")
                st.rerun()  # 페이지 새로고침
            else:  # 탈퇴 실패
                st.error("탈퇴 실패")