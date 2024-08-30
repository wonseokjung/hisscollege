import streamlit as st
import pandas as pd

# 간단한 인증 시스템
def check_password():
    if 'password_correct' not in st.session_state:
        st.session_state.password_correct = False
    
    if not st.session_state.password_correct:
        password = st.text_input("비밀번호를 입력하세요", type="password")
        if password == "hisscollege":  # 실제 사용 시 더 안전한 방식으로 변경해야 합니다
            st.session_state.password_correct = True
        else:
            st.error("비밀번호가 틀렸습니다.")
    
    return st.session_state.password_correct

# 관리자 대시보드
def admin_dashboard():
    st.title("HISS COLLEGE 관리자 대시보드")
    
    # 샘플 학생 데이터
    students = pd.DataFrame({
        "이름": ["John Doe", "Jane Smith", "Alex Johnson"],
        "목표": ["AI 웹서비스 개발", "스페인어 마스터", "피트니스 프로그램"],
        "진행률": [0.75, 0.60, 0.40],
        "시작일": ["2023-01-01", "2023-02-15", "2023-03-10"]
    })
    
    st.dataframe(students)
    
    st.subheader("학생 진행률")
    st.bar_chart(students.set_index("이름")["진행률"])
    
    st.write("자세한 학생 목록과 개별 대시보드는 왼쪽 사이드바의 페이지에서 확인할 수 있습니다.")

# 메인 앱
def main():
    st.set_page_config(page_title="HISS COLLEGE 관리 시스템", layout="wide")
    
    if check_password():
        admin_dashboard()

if __name__ == "__main__":
    main()