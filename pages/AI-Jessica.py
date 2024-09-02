import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

PASSWORDS = {
    "AI-Jessica": "jessica000",
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

def generate_progress():
    return {
        "Python Development": 0,
        "AI Development": 0,
        "AI Theory": 0,
        "AI Application": 0
    }

def show_jessica_page():
    if not password_protection("AI-Jessica"):
        return

    st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

    # Custom CSS
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
    .goal-container {
        background-color: #4CAF50;
        color: white;
        padding: 20px;
        border-radius: 5px;
        margin-bottom: 20px;
        font-size: 24px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

    # GOAL
    st.markdown('<div class="goal-container">GOAL: Develop Game AI and AI Service for Business in 16 weeks</div>', unsafe_allow_html=True)

    st.title("HISS COLLEGE: Jessica's AI Learning Journey")

    # Student Information
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**Name:** Jessica Legere<br>**Major:** Artificial Intelligence<br>**Language:** English", unsafe_allow_html=True)
    with col2:
        st.markdown("**Student ID:** AI22001<br>**Year:** 1st Year<br>**Specialization:** AI Entrepreneurship", unsafe_allow_html=True)
    with col3:
        st.markdown("**Email:** jlegere07@gmail.com<br>**Goal:** Game AI & AI Service for Business", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Current Goal and Curriculum
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    st.header("Current Program Details")
    st.markdown("""
    <div style='background-color: #e9ecef; padding: 15px; border-radius: 5px; margin-bottom: 20px;'>
    <h2 style='margin:0; color: black;'>Current Goal: Develop Game AI and AI Business Service</h2>
    <h3 style='margin:5px 0 0 0; color: black;'>Program Duration: 16 weeks</h3>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("16-Week Curriculum Overview")
    curriculum = [
        "Week 1: Introduction to Google Colab and OpenAI API",
        "Week 2: Developing a game AI agent using Reinforcement Learning - Part 1",
        "Week 3: Developing a game AI agent using Reinforcement Learning - Part 2",
        "Week 4: Introduction to Web Development with Wix - Part 1",
        "Week 5: Introduction to Web Development with Wix - Part 2",
        "Week 6: Integrating OpenAI API into Wix website - Part 1",
        "Week 7: Integrating OpenAI API into Wix website - Part 2",
        "Week 8: Developing a chatbot for the web service - Part 1",
        "Week 9: Developing a chatbot for the web service - Part 2",
        "Week 10: Enhancing UI/UX of the web service - Part 1",
        "Week 11: Enhancing UI/UX of the web service - Part 2",
        "Week 12: Implementing additional AI features - Part 1",
        "Week 13: Implementing additional AI features - Part 2",
        "Week 14: Testing and debugging the web service - Part 1",
        "Week 15: Testing and debugging the web service - Part 2",
        "Week 16: Finalizing the project and preparing for deployment"
    ]

    completed_weeks = []

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
    weeks_data = {week: generate_progress() for week in range(1, 17)}
    df = pd.DataFrame(weeks_data).T
    df.index.name = 'Week'

    # Interactive Week Selection
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    selected_week = st.slider("Select Week", min_value=1, max_value=16, value=1)
    
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    st.header("Message From AI Professor")
    st.markdown("""
    <div style="display: flex; justify-content: center; margin-top: 20px;">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/mxUKxb1SUJs?si=B4OxUxqbRwiKV0CU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)



    
    # Weekly Mission
    st.header("Weekly Mission")
    mission_box = st.container()

    weekly_missions = {
        1: {
            "missions": [
                "Set up Google Colab environment",
                "Create a new Colab notebook and run basic Python code",
                "Install and import the OpenAI library in Colab",
                "Create a simple script to call the OpenAI API and generate text",
                "Experiment with different AI models available through the OpenAI API"
            ],
        },
        2: {
            "missions": [
                "Research reinforcement learning concepts",
                "Set up the game environment in Colab",
                "Implement a basic reinforcement learning agent for the game",
                "Train the agent and observe its performance",
                "Optimize the agent's performance"
            ],
        },
        # Add more weeks as needed
    }

    with mission_box:
        st.markdown(f"""
        <div style='background-color: #e9ecef; padding: 20px; border-radius: 5px; border: 2px solid black;'>
        <h3 style='color: black; margin-top: 0;'>Week {selected_week} Mission:</h3>
        <ul>
        {"".join(f"<li>{mission}</li>" for mission in weekly_missions.get(selected_week, {}).get("missions", ["No specific mission for this week."]))}
        </ul>
        <p><strong>Remember:</strong> Each step brings you closer to your AI startup goal. Stay focused and enjoy the learning process!</p>
        </div>
        """, unsafe_allow_html=True)


    st.markdown("""
    <div style="text-align: center; margin-top: 20px; margin-bottom: 20px;">
        <a href="https://jaijung.notion.site/LV-1-Basic-Python-Mission-Learning-Korean-Pop-Basic-Python-code-e2e38102996f44f8abe2f97218903cd4" target="_blank">
            <button style="font-size: 18px; padding: 10px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer;">
                View this week Mission!
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

    # YouTube 비디오 임베딩
    st.markdown("""
    <div style="display: flex; justify-content: center; margin-top: 20px;">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/RLYoEyIHL6A" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
    """, unsafe_allow_html=True)

    # Current Stats
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    st.header(f"Week {selected_week} Stats")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Python Development", f"{df.loc[selected_week, 'Python Development']}%", "")
    col2.metric("AI Development", f"{df.loc[selected_week, 'AI Development']}%", "")
    col3.metric("AI Theory", f"{df.loc[selected_week, 'AI Theory']}%", "")
    col4.metric("AI Application", f"{df.loc[selected_week, 'AI Application']}%", "")
    st.markdown('</div>', unsafe_allow_html=True)

    # Comprehensive Progress Visualization
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    st.header("AI Learning Progress Dashboard")

    fig = make_subplots(rows=1, cols=2, 
                        subplot_titles=("Skill Progress", "Weekly Comparison"),
                        column_widths=[0.7, 0.3])

    # Skill Progress
    fig.add_trace(go.Scatter(x=df.index, y=df['Python Development'], mode='lines+markers', name='Python Development', line=dict(color='#FF6B6B')), row=1, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=df['AI Development'], mode='lines+markers', name='AI Development', line=dict(color='#4ECDC4')), row=1, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=df['AI Theory'], mode='lines+markers', name='AI Theory', line=dict(color='#FFD93D')), row=1, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=df['AI Application'], mode='lines+markers', name='AI Application', line=dict(color='#6BCB77')), row=1, col=1)

    # Weekly Comparison
    categories = ['Python Development', 'AI Development', 'AI Theory', 'AI Application']
    fig.add_trace(go.Bar(x=categories, y=[0, 0, 0, 0], name=f'Week {selected_week}', marker_color='#4D96FF'), row=1, col=2)

    fig.update_layout(height=400, width=800, title_text="Jessica's AI Learning Journey", showlegend=True)
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    st.plotly_chart(fig)


    # Learning Focus Distribution (as a separate chart)
    focus_data = pd.DataFrame({
        'Category': ['Python Development', 'AI Development', 'AI Theory', 'AI Application'],
        'Percentage': [25, 25, 25, 25]
    })
    fig_pie = px.pie(focus_data, values='Percentage', names='Category', title='Learning Focus Distribution')
    st.plotly_chart(fig_pie)

    st.markdown('</div>', unsafe_allow_html=True)

    # Weekly Notes
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    st.header("Weekly Insights")
    weekly_notes = {
        1: "Starting the AI program. Setting up the environment and getting familiar with the tools we'll be using throughout the course.",
        2: "No progress yet. This week's tasks are yet to be completed.",
    }
    st.write(weekly_notes.get(selected_week, "No notes available for this week."))

    # Motivation Quote
    st.markdown('<div style="background-color: black; color: white; padding: 10px; border-radius: 5px;">"The best way to predict the future is to create it." - Peter Drucker</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

show_jessica_page()