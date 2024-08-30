import streamlit as st
import pandas as pd
import plotly.express as px
import random

st.title("HISS COLLEGE 학생 대시보드")

# 샘플 학생 데이터 (실제로는 데이터베이스에서 가져와야 함)
students = pd.DataFrame({
    "이름": ["John Doe", "Jane Smith", "Alex Johnson"],
    "목표": ["AI 웹서비스 개발", "스페인어 마스터", "피트니스 프로그램"],
    "진행률": [0.75, 0.60, 0.40],
    "시작일": ["2023-01-01", "2023-02-15", "2023-03-10"]
})

if 'selected_student' not in st.session_state:
    st.warning("학생 목록 페이지에서 학생을 선택해주세요.")
else:
    student_name = st.session_state.selected_student
    student = students[students['이름'] == student_name].iloc[0]
    
    st.subheader(f"{student_name}의 학습 현황")
    st.write(f"목표: {student['목표']}")
    st.write(f"시작일: {student['시작일']}")

    progress = student['진행률']
    st.progress(progress)
    st.write(f"전체 진행률: {progress*100:.1f}%")

    # 주간 학습 시간 그래프
    weeks = list(range(1, 11))
    hours = [random.randint(5, 30) for _ in weeks]
    df = pd.DataFrame({"주차": weeks, "학습시간": hours})
    fig = px.line(df, x="주차", y="학습시간", title="주간 학습 시간")
    st.plotly_chart(fig)

    # 다음 과제
    st.subheader("다음 과제")
    tasks = ["AI 모델 구현", "데이터베이스 최적화", "UI/UX 개선", "성능 테스트"]
    for task in random.sample(tasks, 3):
        st.write(f"- {task}")

    # 성취 뱃지
    st.subheader("획득한 뱃지")
    badges = ["🥇 빠른 학습자", "🏆 꾸준한 출석", "🌟 우수한 과제"]
    cols = st.columns(3)
    for idx, badge in enumerate(random.sample(badges, 3)):
        cols[idx].metric(badge, "획득")