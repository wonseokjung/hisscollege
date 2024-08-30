import streamlit as st
import pandas as pd

st.title("HISS COLLEGE 학생 목록")

# 샘플 학생 데이터
students = pd.DataFrame({
    "이름": ["John Doe", "Jane Smith", "Alex Johnson"],
    "목표": ["AI 웹서비스 개발", "스페인어 마스터", "피트니스 프로그램"],
    "진행률": [0.75, 0.60, 0.40],
    "시작일": ["2023-01-01", "2023-02-15", "2023-03-10"]
})

for _, student in students.iterrows():
    with st.expander(f"{student['이름']} - {student['목표']}"):
        st.write(f"진행률: {student['진행률']*100:.0f}%")
        st.write(f"시작일: {student['시작일']}")
        if st.button(f"{student['이름']}의 상세 정보 보기", key=student['이름']):
            st.session_state.selected_student = student['이름']
            st.experimental_rerun()