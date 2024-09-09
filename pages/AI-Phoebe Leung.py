import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

PASSWORDS = {
    "AI-Phoebe": "phoebe000",
    # Add other students' passwords here
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
        "Python Basics": 0,
        "Problem Solving": 0,
        "Data Handling": 0,
        "AI Creativity": 0
    }

def show_phoebe_page():
    if not password_protection("AI-Phoebe"):
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
    st.markdown('<div class="goal-container">GOAL: Master Python Basics and Create with AI in 16 weeks</div>', unsafe_allow_html=True)

    st.title("HISS COLLEGE: Phoebe's AI Learning Journey")

    # Student Information
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**Name:** Phoebe Leung<br>**Major:** Artificial Intelligence<br>**Language:** English", unsafe_allow_html=True)
    with col2:
        st.markdown("**Background:** Economics, Accountant<br>**Field:** Humanitarian Aid<br>**Specialization:** AI for Humanitarian Efforts", unsafe_allow_html=True)
    with col3:
        st.markdown("**Email:** kwp.leung@gmail.com<br>**Goal:** Apply AI in Humanitarian Aid", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Current Goal and Curriculum
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    st.header("Current Program Details")
    st.markdown("""
    <div style='background-color: #e9ecef; padding: 15px; border-radius: 5px; margin-bottom: 20px;'>
    <h2 style='margin:0; color: black;'>Current Goal: Master Python Basics and Create with AI</h2>
    <h3 style='margin:5px 0 0 0; color: black;'>Program Duration: 16 weeks</h3>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("16-Week Curriculum Overview")
    curriculum = [
        "Week 1: Introduction to Python and Google Colab",
        "Week 2: Variables, Data Types, and Basic Operations",
        "Week 3: Control Structures (if statements, loops)",
        "Week 4: Functions and Modules",
        "Week 5: Lists and Tuples",
        "Week 6: Dictionaries and Sets",
        "Week 7: File Handling and Exception Handling",
        "Week 8: Object-Oriented Programming Basics",
        "Week 9: Working with Libraries (NumPy, Pandas)",
        "Week 10: Data Visualization with Matplotlib",
        "Week 11: Web Scraping Basics",
        "Week 12: Introduction to API Usage",
        "Week 13: AI for Image Generation",
        "Week 14: AI for Music Creation",
        "Week 15: AI for Video Production",
        "Week 16: Final Project: Creating a Multi-media AI Application"
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
        <iframe width="560" height="315" src="https://www.youtube.com/embed/_t8v9Drz4KY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
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
                "Learn basic Python syntax",
                "Create your first Python script",
                "Explore data types in Python",
                "Complete exercises in the provided Colab notebook"
            ],
        },
        # Add more weeks as needed
    }

    with mission_box:
        st.markdown(f"""
        <div style='background-color: #e9ecef; padding: 20px; border-radius: 5px; border: 2px solid black;'>
        <h3 style='color: black; margin-top: 0;'>Week {selected_week} Mission:</h3>
        <ul>
        {"".join(f"<li>{mission}</li>" for mission in weekly_missions.get(selected_week, {}).get("missions", ["No specific mission for this week yet."]))}
        </ul>
        <p><strong>Remember:</strong> Consistency is key in learning programming. Dedicate time each day to practice!</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="text-align: center; margin-top: 20px; margin-bottom: 20px;">
        <a href="https://jaijung.notion.site/LV-1-Basic-Python-Mission-Learning-Korean-Pop-Basic-Python-code-e2e38102996f44f8abe2f97218903cd4" target="_blank">
            <button style="font-size: 18px; padding: 10px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer;">
                View this week's Mission!
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

    # Current Stats
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    st.header(f"Week {selected_week} Stats")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Python Basics", f"{df.loc[selected_week, 'Python Basics']}%", "")
    col2.metric("Problem Solving", f"{df.loc[selected_week, 'Problem Solving']}%", "")
    col3.metric("Data Handling", f"{df.loc[selected_week, 'Data Handling']}%", "")
    col4.metric("AI Creativity", f"{df.loc[selected_week, 'AI Creativity']}%", "")
    st.markdown('</div>', unsafe_allow_html=True)

    # Comprehensive Progress Visualization
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    st.header("AI Learning Progress Dashboard")

    fig = make_subplots(rows=1, cols=2, 
                        subplot_titles=("Skill Progress", "Weekly Comparison"),
                        column_widths=[0.7, 0.3])

    # Skill Progress
    fig.add_trace(go.Scatter(x=df.index, y=df['Python Basics'], mode='lines+markers', name='Python Basics', line=dict(color='#FF6B6B')), row=1, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=df['Problem Solving'], mode='lines+markers', name='Problem Solving', line=dict(color='#4ECDC4')), row=1, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=df['Data Handling'], mode='lines+markers', name='Data Handling', line=dict(color='#FFD93D')), row=1, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=df['AI Creativity'], mode='lines+markers', name='AI Creativity', line=dict(color='#6BCB77')), row=1, col=1)

    # Weekly Comparison
    categories = ['Python Basics', 'Problem Solving', 'Data Handling', 'AI Creativity']
    fig.add_trace(go.Bar(x=categories, y=[0, 0, 0, 0], name=f'Week {selected_week}', marker_color='#4D96FF'), row=1, col=2)

    fig.update_layout(height=400, width=800, title_text="Phoebe's AI Learning Journey", showlegend=True)
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    st.plotly_chart(fig)

    # Learning Focus Distribution (as a separate chart)
    focus_data = pd.DataFrame({
        'Category': ['Python Basics', 'Problem Solving', 'Data Handling', 'AI Creativity'],
        'Percentage': [40, 25, 25, 10]
    })
    fig_pie = px.pie(focus_data, values='Percentage', names='Category', title='Learning Focus Distribution')
    st.plotly_chart(fig_pie)

    st.markdown('</div>', unsafe_allow_html=True)

    # Weekly Notes
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    st.header("Weekly Insights")
    weekly_notes = {
        1: "Introduced to Google Colab and basic Python concepts. Focus on building a strong foundation in programming.",
    }
    st.write(weekly_notes.get(selected_week, "No notes available for this week yet."))

    # Motivation Quote
    st.markdown('<div style="background-color: black; color: white; padding: 10px; border-radius: 5px;">"The only way to learn a new programming language is by writing programs in it." - Dennis Ritchie</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

show_phoebe_page()