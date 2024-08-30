import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

PASSWORDS = {
    "Jaymi": "jaymi123",
    "John": "john123",
    # 다른 학생들의 비밀번호도 여기에 추가
}

def password_protection(student_name):
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        password = st.text_input("Enter password", type="password")
        if st.button("Login"):
            if password == PASSWORDS.get(student_name):
                st.session_state.authenticated = True
                st.experimental_rerun()  # 이 부분을 제거하고 아래와 같이 바꿉니다.
            else:
                st.error("Incorrect password")
        return False
    return True

def show_jaymi_page():
    if not password_protection("Jaymi"):
        return

    st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

    # Hide sidebar and footer
    st.markdown("""
    <style>
    .css-1d391kg {width: 0px;}
    .css-1it9etk {display: none;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)


    st.title("🏋️‍♀️ HISS COLLEGE: Jaymi's Fitness Journey 🏋️‍♀️")

    # Student Information
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("**Name:** Jaymi Green\n**Major:** Fitness\n**Language:** English")
    with col2:
        st.info("**Height:** 178 cm\n**Gender:** Female\n**Date of Birth:** October 31, 1981")
    with col3:
        st.info("**Email:** jaymi_green1@hotmail.com\n**Goal:** Weight loss & Muscle gain")

    # Current Goal and Curriculum
    st.header("Current Program Details")
    st.markdown("""
    <div style='background-color: #f0f2f6; padding: 15px; border-radius: 10px; margin-bottom: 20px;'>
    <h2 style='margin:0; color: #1e3d59;'>Current Goal: Weight 85kg</h2>
    <h3 style='margin:5px 0 0 0; color: #1e3d59;'>Program Duration: 20 weeks</h3>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("20-Week Curriculum Overview")
    curriculum = [
        "Weeks 1-4: Foundation building and habit formation",
        "Week 5: Lower Body Focus - Leg strength and stability",
        "Week 6: Full Body Conditioning",
        "Week 7: Upper Body Emphasis - Arm and shoulder sculpting",
        "Week 8: Core Power - Abdominal and back strengthening",
        "Week 9: Cardiovascular Endurance Boost",
        "Week 10: Flexibility and Mobility Improvement",
        "Week 11: High-Intensity Interval Training (HIIT) Introduction",
        "Week 12: Balance and Coordination Enhancement",
        "Week 13: Strength Training Intensification",
        "Week 14: Metabolic Conditioning",
        "Week 15: Functional Fitness Focus",
        "Week 16: Power and Plyometrics",
        "Week 17: Active Recovery and Yoga Integration",
        "Week 18: Sports-Specific Training",
        "Week 19: Peak Performance Preparation",
        "Week 20: Final Assessment and Future Planning"
    ]
    for item in curriculum:
        st.markdown(f"<div style='background-color: #e8f1f5; padding: 10px; border-radius: 5px; margin-bottom: 5px;'><b>{item}</b></div>", unsafe_allow_html=True)

    # Weekly Progress Data
    weeks_data = {
        1: {"Knee Push-ups": 0, "Squat Holding": 0, "Burpees": 0, "Plank Holding": 0, "Weight": 98.2, "Energy Level": 6, "Sleep Quality": 6.5},
        2: {"Knee Push-ups": 0, "Squat Holding": 0, "Burpees": 0, "Plank Holding": 0, "Weight": 97.5, "Energy Level": 7, "Sleep Quality": 7.0},
        3: {"Knee Push-ups": 0, "Squat Holding": 0, "Burpees": 0, "Plank Holding": 0, "Weight": 97.8, "Energy Level": 8, "Sleep Quality": 7.5}
    }

    df = pd.DataFrame(weeks_data).T
    df.index.name = 'Week'

    # Interactive Week Selection
    selected_week = st.slider("Select Week", min_value=1, max_value=len(weeks_data), value=len(weeks_data))

    # Weekly Mission
    st.header("Weekly Mission")
    mission_box = st.container()
    
    weekly_missions = {
        1: [
            "Complete 3 core strengthening sessions (Mon, Wed, Fri)",
            "Perform leg workout twice (Tue, Thu) - 12 minutes each session",
            "Achieve 7,000 steps daily",
            "Follow the nutrition plan: 1800-2000 kcal/day, 30% protein, 40% carbs, 30% fats",
            "Implement a bedtime routine for better sleep quality"
        ],
        2: [
            "Increase core sessions to 4 times a week",
            "Add 15 minutes of cardio after each strength training session",
            "Try yoga or stretching twice this week for flexibility",
            "Increase daily step goal to 8,000",
            "Focus on increasing protein intake to 1.8g per kg of body weight"
        ],
        3: [
            "Introduce HIIT workouts twice a week",
            "Continue with 3 strength training sessions",
            "Attempt a 5km walk or light jog",
            "Practice mindful eating and log all meals",
            "Aim for 8 hours of sleep each night"
        ]
    }

    with mission_box:
        st.markdown(f"""
        <div style='background-color: #e6f3ff; padding: 20px; border-radius: 10px; border: 2px solid #3399ff;'>
        <h3 style='color: #3399ff; margin-top: 0;'>Week {selected_week} Mission:</h3>
        <ul>
        {"".join(f"<li>{mission}</li>" for mission in weekly_missions.get(selected_week, ["No specific mission for this week."]))}
        </ul>
        <p><strong>Remember:</strong> Listen to your body and adjust as needed. Your health and safety come first!</p>
        </div>
        """, unsafe_allow_html=True)

    # Current Stats
    st.header(f"Week {selected_week} Stats")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Knee Push-ups", f"{df.loc[selected_week, 'Knee Push-ups']} reps", f"{df.loc[selected_week, 'Knee Push-ups'] - df.loc[1, 'Knee Push-ups']} from start")
    col2.metric("Squat Holding", f"{df.loc[selected_week, 'Squat Holding']} sec", f"{df.loc[selected_week, 'Squat Holding'] - df.loc[1, 'Squat Holding']} from start")
    col3.metric("Burpees", f"{df.loc[selected_week, 'Burpees']} reps", f"{df.loc[selected_week, 'Burpees'] - df.loc[1, 'Burpees']} from start")
    col4.metric("Plank Holding", f"{df.loc[selected_week, 'Plank Holding']} sec", f"{df.loc[selected_week, 'Plank Holding'] - df.loc[1, 'Plank Holding']} from start")

    # Comprehensive Progress Visualization
    st.header("Fitness Progress Dashboard")

    fig = make_subplots(rows=2, cols=2, subplot_titles=("Weight Progress", "Energy & Sleep", "Strength Metrics", "Endurance Metrics"))

    # Weight Progress
    fig.add_trace(go.Scatter(x=df.index, y=df['Weight'], mode='lines+markers', name='Weight'), row=1, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=[85]*len(df), mode='lines', name='Goal Weight', line=dict(dash='dash')), row=1, col=1)

    # Energy & Sleep
    fig.add_trace(go.Scatter(x=df.index, y=df['Energy Level'], mode='lines+markers', name='Energy Level'), row=1, col=2)
    fig.add_trace(go.Scatter(x=df.index, y=df['Sleep Quality'], mode='lines+markers', name='Sleep Quality'), row=1, col=2)

    # Strength Metrics
    fig.add_trace(go.Bar(x=df.index, y=df['Knee Push-ups'], name='Knee Push-ups'), row=2, col=1)
    fig.add_trace(go.Bar(x=df.index, y=df['Burpees'], name='Burpees'), row=2, col=1)

    # Endurance Metrics
    fig.add_trace(go.Bar(x=df.index, y=df['Squat Holding'], name='Squat Holding'), row=2, col=2)
    fig.add_trace(go.Bar(x=df.index, y=df['Plank Holding'], name='Plank Holding'), row=2, col=2)

    fig.update_layout(height=800, width=1000, title_text="Jaymi's Fitness Journey")
    st.plotly_chart(fig)

    # Radar Chart for Overall Progress
    st.subheader("Overall Progress (Relative to Starting Point)")
    categories = ['Knee Push-ups', 'Squat Holding', 'Burpees', 'Plank Holding', 'Energy Level', 'Sleep Quality']
    fig_radar = go.Figure(data=go.Scatterpolar(
        r=[df.loc[selected_week, cat] / df.loc[1, cat] * 100 for cat in categories],
        theta=categories,
        fill='toself',
        name=f'Week {selected_week} Progress'
    ))
    fig_radar.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 150])),
        showlegend=False
    )
    st.plotly_chart(fig_radar)

    # Weekly Notes
    st.header("Weekly Insights")
    weekly_notes = {
        1: "Started the program. Feeling motivated but challenged.",
        2: "Improved energy levels. Core exercises are getting easier.",
        3: "Struggled with leg workouts. Overall energy levels have increased significantly."
    }
    st.write(weekly_notes.get(selected_week, "No notes available for this week."))

    # Motivation Quote
    st.success("The only bad workout is the one that didn't happen. - Jay Jung")

show_jaymi_page()
