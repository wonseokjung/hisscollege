import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

PASSWORDS = {
    "Jaymi": "jaymi123",
    
    # 다른 학생들의 비밀번호도 여기에 추가
}

def password_protection(student_name):
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        password = st.text_input("Enter password, Click Log in x2", type="password")
        if st.button("Login"):
            if password == PASSWORDS.get(student_name):
                st.session_state.authenticated = True
            else:
                st.error("Incorrect password")
                st.stop()
        return False
    return True

def show_jaymi_page():
    if not password_protection("Jaymi"):
        return

    st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

    # Custom CSS for black and white theme with colorful graphs
    st.markdown("""
    <style>
    .css-1d391kg {width: 0px;}
    .css-1it9etk {display: none;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp {
        background-color: white;
        color: black;
    }
    .custom-container {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: black;
        color: white;
    }
    .stTextInput>div>div>input {
        color: black;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("HISS COLLEGE: Jaymi's Fitness Journey")

    # Student Information
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**Name:** Jaymi Green<br>**Major:** Fitness<br>**Language:** English", unsafe_allow_html=True)
    with col2:
        st.markdown("**Height:** 178 cm<br>**Gender:** Female<br>**Date of Birth:** October 31, 1981", unsafe_allow_html=True)
    with col3:
        st.markdown("**Email:** jaymi_green1@hotmail.com<br>**Goal:** Weight loss & Muscle gain", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Current Goal and Curriculum
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    st.header("Current Program Details")
    st.markdown("""
    <div style='background-color: #e9ecef; padding: 15px; border-radius: 5px; margin-bottom: 20px;'>
    <h2 style='margin:0; color: black;'>Current Goal: Weight 85kg</h2>
    <h3 style='margin:5px 0 0 0; color: black;'>Program Duration: 20 weeks</h3>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("20-Week Curriculum Overview")
    curriculum = [
        "Week 1: Core Strengthening - Foundation building",
        "Week 2: Core + Leg - Enhancing lower body strength",
        "Week 3: Core + Leg + Shoulder - Upper body introduction",
        "Week 4: Burpees - Full body conditioning and endurance",
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

    completed_weeks = [1, 2]

    for index, item in enumerate(curriculum, start=1):
        completion_status = "✅" if index in completed_weeks else "⬜"
        
        st.markdown(
            f"""
            <div style='display: flex; justify-content: space-between; align-items: center; background-color: {'#e9ecef' if index % 2 == 0 else 'white'}; padding: 10px; border-radius: 5px; margin-bottom: 5px;'>
                <span style='flex-grow: 1;'><b>{item}</b></span>
                <span style='margin-left: 10px;'>{completion_status}</span>
            </div>
            """, 
            unsafe_allow_html=True
        )
    st.markdown('</div>', unsafe_allow_html=True)

    # Weekly Progress Data
    weeks_data = {
        1: {"Knee Push-ups": 0, "Squat Holding": 0, "Burpees": 0, "Plank Holding": 0, "Weight": 98.2, "Energy Level": 6, "Sleep Quality": 6.5},
        2: {"Knee Push-ups": 0, "Squat Holding": 0, "Burpees": 0, "Plank Holding": 0, "Weight": 97.5, "Energy Level": 7, "Sleep Quality": 7.0},
    }

    df = pd.DataFrame(weeks_data).T
    df.index.name = 'Week'

    # Interactive Week Selection
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    selected_week = st.slider("Select Week", min_value=1, max_value=len(weeks_data), value=len(weeks_data))
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    st.header("Message From Jay Professor")
    professor_messages = {
        1: "https://www.youtube.com/embed/n2cUsooRDv4",
        2: "https://www.youtube.com/embed/n2cUsooRDv4",
        # 추가 주차의 메시지 영상 URL을 여기에 추가할 수 있습니다.
    }
    
    message_url = professor_messages.get(selected_week)
    if message_url:
        st.markdown(f"""
        <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
          <iframe src="{message_url}" 
                 style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" 
                 frameborder="0" 
                 allow="autoplay; encrypted-media" 
                 allowfullscreen>
          </iframe>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.write("No message available for this week.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Weekly Mission
    st.header("Weekly Mission")
    mission_box = st.container()
    
    weekly_missions = {
        1: {
            "missions": [
                "Complete 3 core strengthening sessions (Mon, Wed, Fri)",
                "Perform leg workout twice (Tue, Thu) - 12 minutes each session",
                "Achieve 7,000 steps daily",
                "Follow the nutrition plan: 1800-2000 kcal/day, 30% protein, 40% carbs, 30% fats",
                "Implement a bedtime routine for better sleep quality"
            ],
            "video_url": ""
        },
        2: {
            "missions": [
                "Increase core sessions to 4 times a week",
                "Add 15 minutes of cardio after each strength training session",
                "Try yoga or stretching twice this week for flexibility",
                "Increase daily step goal to 8,000",
                "Focus on increasing protein intake to 1.8g per kg of body weight"
            ],
            "video_url": "https://www.youtube.com/embed/xW19K-uhOGk"
        },
    }

    with mission_box:
        st.markdown(f"""
        <div style='background-color: #e9ecef; padding: 20px; border-radius: 5px; border: 2px solid black;'>
        <h3 style='color: black; margin-top: 0;'>Week {selected_week} Mission:</h3>
        <ul>
        {"".join(f"<li>{mission}</li>" for mission in weekly_missions.get(selected_week, {}).get("missions", ["No specific mission for this week."]))}
        </ul>
        <p><strong>Remember:</strong> Listen to your body and adjust as needed. Your health and safety come first!</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Display embedded video for the selected week
        video_url = weekly_missions.get(selected_week, {}).get("video_url")
        if video_url:
            st.markdown(f"""
            <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
              <iframe src="{video_url}" 
                     style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" 
                     frameborder="0" 
                     allow="autoplay; encrypted-media" 
                     allowfullscreen>
              </iframe>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.write("No video available for this week.")

    st.markdown('</div>', unsafe_allow_html=True)

    # Current Stats
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    st.header(f"Week {selected_week} Stats")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Knee Push-ups", f"{df.loc[selected_week, 'Knee Push-ups']} reps", f"{df.loc[selected_week, 'Knee Push-ups'] - df.loc[1, 'Knee Push-ups']} from start")
    col2.metric("Squat Holding", f"{df.loc[selected_week, 'Squat Holding']} sec", f"{df.loc[selected_week, 'Squat Holding'] - df.loc[1, 'Squat Holding']} from start")
    col3.metric("Burpees", f"{df.loc[selected_week, 'Burpees']} reps", f"{df.loc[selected_week, 'Burpees'] - df.loc[1, 'Burpees']} from start")
    col4.metric("Plank Holding", f"{df.loc[selected_week, 'Plank Holding']} sec", f"{df.loc[selected_week, 'Plank Holding'] - df.loc[1, 'Plank Holding']} from start")
    st.markdown('</div>', unsafe_allow_html=True)

    # Comprehensive Progress Visualization
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    st.header("Fitness Progress Dashboard")

    fig = make_subplots(rows=3, cols=2, subplot_titles=("Weight Progress", "Energy & Sleep", "Strength Metrics", "Endurance Metrics", "Daily Steps"))

    # Weight Progress
    fig.add_trace(go.Scatter(x=df.index, y=df['Weight'], mode='lines+markers', name='Weight', line=dict(color='#FF6B6B')), row=1, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=[85]*len(df), mode='lines', name='Goal Weight', line=dict(dash='dash', color='#4ECDC4')), row=1, col=1)

    # Energy & Sleep
    fig.add_trace(go.Scatter(x=df.index, y=df['Energy Level'], mode='lines+markers', name='Energy Level', line=dict(color='#FFD93D')), row=1, col=2)
    fig.add_trace(go.Scatter(x=df.index, y=df['Sleep Quality'], mode='lines+markers', name='Sleep Quality', line=dict(color='#6BCB77')), row=1, col=2)

    # Strength Metrics
    fig.add_trace(go.Bar(x=df.index, y=df['Knee Push-ups'], name='Knee Push-ups', marker_color='#4D96FF'), row=2, col=1)
    fig.add_trace(go.Bar(x=df.index, y=df['Burpees'], name='Burpees', marker_color='#6BCB77'), row=2, col=1)

    # Endurance Metrics
    fig.add_trace(go.Bar(x=df.index, y=df['Squat Holding'], name='Squat Holding', marker_color='#FF6B6B'), row=2, col=2)
    fig.add_trace(go.Bar(x=df.index, y=df['Plank Holding'], name='Plank Holding', marker_color='#FFD93D'), row=2, col=2)
    # Daily Steps (New)
    daily_steps = [7500, 8200]  # Example data
    fig.add_trace(go.Scatter(x=df.index, y=daily_steps, mode='lines+markers', name='Daily Steps', line=dict(color='#FF9999')), row=3, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=[10000]*len(df), mode='lines', name='Step Goal', line=dict(dash='dash', color='#66B2FF')), row=3, col=1)

    fig.update_layout(height=1000, width=1000, title_text="Jaymi's Fitness Journey", plot_bgcolor='white', paper_bgcolor='white')
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    st.plotly_chart(fig)

    # Nutrition (New) - Separate Pie Chart
    st.subheader("Nutrition Breakdown")
    nutrition_data = pd.DataFrame({
        'Category': ['Protein', 'Carbs', 'Fats'],
        'Percentage': [30, 40, 30]
    })
    fig_pie = px.pie(nutrition_data, values='Percentage', names='Category', title='Nutrition Breakdown',
                     color_discrete_sequence=['#FF6B6B', '#4ECDC4', '#FFD93D'])
    st.plotly_chart(fig_pie)

    # Radar Chart for Overall Progress
    st.subheader("Overall Progress (Relative to Starting Point)")
    categories = ['Knee Push-ups', 'Squat Holding', 'Burpees', 'Plank Holding', 'Energy Level', 'Sleep Quality']
    fig_radar = go.Figure(data=go.Scatterpolar(
        r=[df.loc[selected_week, cat] / df.loc[1, cat] * 100 for cat in categories],
        theta=categories,
        fill='toself',
        name=f'Week {selected_week} Progress',
        line=dict(color='#FF6B6B')
    ))
    fig_radar.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 150])),
        showlegend=False,
        plot_bgcolor='white',
        paper_bgcolor='white'
    )
    st.plotly_chart(fig_radar)

    # Workout Intensity Heatmap (New)
    st.subheader("Workout Intensity Heatmap")
    workout_intensity = pd.DataFrame({
        'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        'Week 1': [3, 2, 3, 2, 3, 1, 0],
        'Week 2': [3, 3, 3, 2, 3, 2, 1],
    })
    fig_heatmap = px.imshow(workout_intensity.set_index('Day'),
                            labels=dict(x="Week", y="Day", color="Intensity"),
                            x=['Week 1', 'Week 2'],
                            y=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                            color_continuous_scale='Viridis')
    fig_heatmap.update_layout(title='Workout Intensity by Day and Week')
    st.plotly_chart(fig_heatmap)

    st.markdown('</div>', unsafe_allow_html=True)

    # Weekly Notes
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    st.header("Weekly Insights")
    weekly_notes = {
        1: "Started the program. Feeling motivated but challenged. Focus on core strengthening and establishing routine.",
        2: "Improved energy levels. Core exercises are getting easier. Introduced leg workouts and increased daily steps."
    }
    st.write(weekly_notes.get(selected_week, "No notes available for this week."))

    # Motivation Quote
    st.markdown('<div style="background-color: black; color: white; padding: 10px; border-radius: 5px;">"The only bad workout is the one that didn\'t happen." - Jay Jung</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

show_jaymi_page()