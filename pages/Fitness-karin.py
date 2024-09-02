import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import numpy as np

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

PASSWORDS = {
    "Karin": "karin111",
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

def calculate_bmi(weight, height):
    return weight / ((height/100) ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def bmi_calculator():
    st.subheader("BMI Calculator")
    
    weight = st.number_input("Enter your weight (kg)", min_value=30.0, max_value=200.0, value=83.4, step=0.1)
    height = st.number_input("Enter your height (cm)", min_value=100.0, max_value=250.0, value=174.0, step=0.1)
    
    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        bmi_category = get_bmi_category(bmi)
        
        st.write(f"Your BMI is: {bmi:.2f}")
        st.write(f"Category: {bmi_category}")
        
        # Create BMI graph
        fig = go.Figure()
        
        # BMI ranges
        bmi_ranges = [
            (0, 18.5, "Underweight", "blue"),
            (18.5, 25, "Normal", "green"),
            (25, 30, "Overweight", "orange"),
            (30, 40, "Obese", "red")
        ]
        
        for start, end, label, color in bmi_ranges:
            fig.add_shape(
                type="rect",
                x0=start, x1=end, y0=0, y1=1,
                fillcolor=color,
                opacity=0.3,
                layer="below",
                line_width=0,
            )
            fig.add_annotation(
                x=(start + end) / 2, y=1.05,
                text=label,
                showarrow=False,
            )
        
        # Add marker for current BMI
        fig.add_trace(go.Scatter(
            x=[bmi],
            y=[0.5],
            mode="markers",
            marker=dict(size=15, color="black", symbol="star"),
            name="Your BMI"
        ))
        
        fig.update_layout(
            title="BMI Chart",
            xaxis_title="BMI",
            yaxis_title="",
            showlegend=False,
            height=400,
            yaxis=dict(showticklabels=False, range=[0, 1.1]),
            xaxis=dict(range=[15, 40]),
        )
        
        st.plotly_chart(fig)

def detailed_nutrition_plan():
    st.header("Detailed Nutrition Plan")

    # More detailed weekly meal plan
    meal_plan = {
        "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "Breakfast": [
            "Greek yogurt (150g) with berries (100g) and granola (30g)",
            "Whole grain toast (2 slices) with avocado (1/2) and eggs (2)",
            "Oatmeal (50g dry) with banana (1 medium) and chia seeds (15g)",
            "Protein pancakes (2) with fresh berries (100g)",
            "Scrambled eggs (3) with spinach (50g) and whole grain toast (1 slice)",
            "Whole grain cereal (50g) with almond milk (250ml) and sliced almonds (30g)",
            "Vegetable omelet (3 eggs) with whole grain toast (1 slice)"
        ],
        "Lunch": [
            "Grilled chicken breast (150g) salad with mixed greens (100g) and vinaigrette (15ml)",
            "Turkey (100g) and vegetable wrap with hummus (30g)",
            "Tuna salad (100g tuna) on whole grain bread (2 slices)",
            "Lentil soup (300ml) with a side salad (100g)",
            "Grilled vegetable (200g) and chickpea (100g) bowl",
            "Grilled shrimp skewers (150g) with brown rice (150g cooked)",
            "Grilled chicken Caesar salad (150g chicken, 100g romaine, light dressing)"
        ],
        "Dinner": [
            "Baked salmon (150g) with quinoa (150g cooked) and roasted vegetables (200g)",
            "Lean beef stir-fry (150g beef) with brown rice (150g cooked)",
            "Grilled tofu (200g) with sweet potato (150g) and broccoli (100g)",
            "Baked chicken breast (150g) with zucchini noodles (200g)",
            "Lean pork tenderloin (150g) with asparagus (100g) and quinoa (150g cooked)",
            "Turkey burger (150g, no bun) with sweet potato fries (100g)",
            "Baked cod (150g) with roasted Brussels sprouts (100g) and wild rice (150g cooked)"
        ],
        "Snack": [
            "Apple slices (1 medium) with almond butter (30g)",
            "Protein smoothie (1 scoop whey, 250ml almond milk, 1 banana)",
            "Carrot sticks (100g) with guacamole (50g)",
            "Greek yogurt (150g) with honey (15g)",
            "Mixed nuts (30g) and dried fruit (20g)",
            "Celery sticks (100g) with peanut butter (30g)",
            "Cottage cheese (150g) with peaches (100g)"
        ],
        "Breakfast_Cal": [350, 400, 350, 300, 350, 400, 350],
        "Lunch_Cal": [400, 450, 400, 350, 400, 450, 400],
        "Dinner_Cal": [500, 550, 450, 400, 500, 450, 450],
        "Snack_Cal": [200, 250, 200, 200, 250, 250, 200]
    }

    df_meal_plan = pd.DataFrame(meal_plan)
    
    # Calculate total calories
    df_meal_plan['Total_Cal'] = df_meal_plan['Breakfast_Cal'] + df_meal_plan['Lunch_Cal'] + df_meal_plan['Dinner_Cal'] + df_meal_plan['Snack_Cal']

    # Calculate approximate macronutrient ratios
    df_meal_plan['Protein'] = df_meal_plan['Total_Cal'] * 0.3 / 4  # 30% of calories from protein
    df_meal_plan['Carbs'] = df_meal_plan['Total_Cal'] * 0.4 / 4    # 40% of calories from carbs
    df_meal_plan['Fat'] = df_meal_plan['Total_Cal'] * 0.3 / 9      # 30% of calories from fat

    st.subheader("Weekly Meal Plan with Calorie Breakdown")
    st.dataframe(df_meal_plan)

    # Daily calorie graph
    st.subheader("Daily Calorie Breakdown")
    fig_calories = px.bar(df_meal_plan, x="Day", y=["Breakfast_Cal", "Lunch_Cal", "Dinner_Cal", "Snack_Cal"],
                          title="Daily Calorie Intake", labels={'value': 'Calories', 'variable': 'Meal'},
                          color_discrete_map={'Breakfast_Cal': '#FFA07A', 'Lunch_Cal': '#98FB98', 
                                              'Dinner_Cal': '#87CEFA', 'Snack_Cal': '#DDA0DD'})
    fig_calories.add_scatter(x=df_meal_plan["Day"], y=df_meal_plan["Total_Cal"], mode="lines+markers", 
                             name="Total Calories", line=dict(color="red", width=2))
    st.plotly_chart(fig_calories)

    # Macronutrient ratio graph
    st.subheader("Daily Macronutrient Breakdown")
    fig_macros = px.bar(df_meal_plan, x="Day", y=["Protein", "Carbs", "Fat"],
                        title="Daily Macronutrient Intake", labels={'value': 'Grams', 'variable': 'Nutrient'},
                        color_discrete_map={'Protein': '#FF6347', 'Carbs': '#32CD32', 'Fat': '#FFD700'})
    st.plotly_chart(fig_macros)

    # Macronutrient ratio pie chart
    st.subheader("Average Macronutrient Ratio")
    avg_macros = df_meal_plan[['Protein', 'Carbs', 'Fat']].mean()
    fig_pie = px.pie(values=avg_macros.values, names=avg_macros.index, 
                     title="Average Macronutrient Ratio",
                     color_discrete_map={'Protein': '#FF6347', 'Carbs': '#32CD32', 'Fat': '#FFD700'})
    st.plotly_chart(fig_pie)

def show_karin_page():
    if not password_protection("Karin"):
        return

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

    st.title("HISS COLLEGE: Karin's Fitness Journey")

    # Student Information
                                                                                                                                                       

    # Current Goal and Curriculum
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    st.header("Current Program Details")
    st.markdown("""
    <div style='background-color: #e9ecef; padding: 15px; border-radius: 5px; margin-bottom: 20px;'>
    <h2 style='margin:0; color: black;'>Current Goal: Weight 78kg</h2>
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

    # Weekly Progress Data 부분에서
    weeks_data = {
        1: {"Knee Push-ups": 0, "Squat Holding": 0, "Burpees": 0, "Plank Holding": 0, "Weight": 83.4, "Energy Level": 6, "Sleep Quality": 6.5},
        2: {"Knee Push-ups": 0, "Squat Holding": 0, "Burpees": 0, "Plank Holding": 0, "Weight": 83.4, "Energy Level": 7, "Sleep Quality": 7.0},
        3: {"Knee Push-ups": 0, "Squat Holding": 0, "Burpees": 0, "Plank Holding": 0, "Weight": 82.5, "Energy Level": 7, "Sleep Quality": 7.5},
    }

    df = pd.DataFrame(weeks_data).T
    df.index.name = 'Week'

    # Interactive Week Selection
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    selected_week = st.slider("Select Week", min_value=1, max_value=3, value=len(weeks_data))
    
    st.header("Message From Jay Professor")
    professor_messages = {
        1: "",
        2: "",
        3: "https://www.youtube.com/embed/VAeeAz-FURY",
        # Add more weekly message video URLs here
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


    # Weekly Mission
    st.header("Weekly Mission")
    mission_box = st.container()
    
    weekly_missions = {
        1: {
            "missions": [
                "Complete 3 core strengthening sessions (Mon, Wed, Fri)",
                "Perform leg workout twice (Tue, Thu) - 12 minutes each session",
                "Achieve 7,000 steps daily",
                "Follow the nutrition plan: 1600-1800 kcal/day, 30% protein, 40% carbs, 30% fats",
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
                "Focus on increasing protein intake to 1.6g per kg of body weight"
            ],
            "video_url": "https://www.youtube.com/embed/xW19K-uhOGk"
        },
        3: {
            "missions": [
                "Goal: Lose 500g this week",
                "Complete the following workout plan:",
                "- Monday: Core (6 min) + Leg (12 min)",
                "- Tuesday: Shoulder (6 min) + Core (6 min)",
                "- Wednesday: Leg (12 min) + Shoulder (6 min)",
                "- Thursday: Core (6 min) + Leg (12 min)",
                "- Friday: Shoulder (6 min) + Core (6 min)",
                "Maintain 8,000 daily steps",
                "Continue following the nutrition plan, aiming for a slight calorie deficit",
                "Get at least 7 hours of sleep each night"
            ],
            "video_url": "https://www.youtube.com/embed/RSDcw4ROhdM"
        }
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
    # Additional: Week 3 workout video links
    if selected_week == 3:
        st.subheader("Week 3 Workout Videos")
        st.markdown("""
        - Core Workout (6 min): [YouTube Link](https://youtu.be/RSDcw4ROhdM?si=NVThuMpc-Gw-bihf)
        - Leg Workout (12 min): [YouTube Link](https://youtu.be/xW19K-uhOGk)
        - Shoulder Workout (6 min): [YouTube Link](https://youtu.be/K8b5HsX1MFc)
        """)

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
    fig.add_trace(go.Scatter(x=df.index, y=[78]*len(df), mode='lines', name='Goal Weight', line=dict(dash='dash', color='#4ECDC4')), row=1, col=1)

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
    daily_steps = [7000, 7500]  # Example data
    fig.add_trace(go.Scatter(x=df.index, y=daily_steps, mode='lines+markers', name='Daily Steps', line=dict(color='#FF9999')), row=3, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=[8000]*len(df), mode='lines', name='Step Goal', line=dict(dash='dash', color='#66B2FF')), row=3, col=1)

    fig.update_layout(height=1000, width=1000, title_text="Karin's Fitness Journey", plot_bgcolor='white', paper_bgcolor='white')
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

    # BMI Calculator and Nutrition Section
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    st.header("BMI and Nutrition")

    # BMI Calculator
    bmi_calculator()
    # Detailed Nutrition Plan
    detailed_nutrition_plan()

    # Nutrition and Meal Plan Section
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    st.header("Nutrition and Meal Plan")

    # Nutritional Recommendations
    st.subheader("Daily Nutritional Intake")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Calories", "1600-1800 kcal")
    col2.metric("Protein", "30% (120-135g)")
    col3.metric("Carbohydrates", "40% (160-180g)")
    col4.metric("Fats", "30% (53-60g)")

    # Nutrition advice based on BMI
    bmi = calculate_bmi(83.4, 174)  # Using Karin's current weight and height
    bmi_category = get_bmi_category(bmi)

    st.subheader("Personalized Nutrition Advice")
    if bmi_category == "Overweight" or bmi_category == "Obese":
        st.write("Based on your current BMI, focus on creating a calorie deficit while maintaining adequate protein intake to preserve muscle mass. Increase your intake of high-fiber foods and lean proteins, and limit processed foods and added sugars.")
    elif bmi_category == "Normal weight":
        st.write("Your BMI is in the normal range. Focus on maintaining a balanced diet with adequate protein for muscle maintenance and growth. Include a variety of fruits, vegetables, whole grains, and lean proteins in your meals.")
    else:  # Underweight
        st.write("Your BMI suggests you might be underweight. Focus on increasing your calorie intake with nutrient-dense foods. Include healthy fats, complex carbohydrates, and protein-rich foods in your diet to support healthy weight gain and muscle growth.")

    # Supplement and Vitamin Recommendations
    st.subheader("Supplement and Vitamin Recommendations")
    supplements = [
        ("Multivitamin", "1 tablet daily with breakfast"),
        ("Omega-3 Fish Oil", "1000mg daily with a meal"),
        ("Vitamin D3", "2000 IU daily"),
        ("Magnesium", "300mg daily before bed"),
        ("Vitamin C", "500mg daily"),
        ("Glucosamine", "1500mg daily for joint health"),
        ("Calcium", "1000mg daily"),
        ("Turmeric", "500mg daily for anti-inflammatory benefits")
    ]

    df_supplements = pd.DataFrame(supplements, columns=["Supplement/Vitamin", "Dosage"])
    st.table(df_supplements)

    # Weekly Meal Plan
    st.subheader("Weekly Meal Plan")
    meal_plan = {
        "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "Breakfast": [
            "Greek yogurt with berries and granola",
            "Whole grain toast with avocado and eggs",
            "Oatmeal with banana and chia seeds",
            "Protein smoothie with spinach and fruit",
            "Scrambled eggs with spinach and whole grain toast",
            "Whole grain cereal with almond milk and sliced almonds",
            "Vegetable omelet with whole grain toast"
        ],
        "Lunch": [
            "Grilled chicken salad with mixed greens and vinaigrette",
            "Lentil soup with a side salad",
            "Tuna salad on whole grain bread",
            "Quinoa and vegetable bowl",
            "Grilled vegetable and chickpea bowl",
            "Turkey and vegetable wrap with hummus",
            "Grilled salmon with roasted vegetables"
        ],
        "Dinner": [
            "Baked cod with quinoa and roasted vegetables",
            "Lean beef stir-fry with brown rice",
            "Grilled tofu with sweet potato and broccoli",
            "Baked chicken breast with zucchini noodles",
            "Vegetarian chili with mixed beans",
            "Grilled shrimp skewers with brown rice",
            "Baked turkey breast with roasted Brussels sprouts and wild rice"
        ],
        "Snack": [
            "Apple slices with almond butter",
            "Carrot sticks with hummus",
            "Greek yogurt with honey",
            "Mixed nuts and dried fruit",
            "Celery with peanut butter",
            "Cottage cheese with peaches",
            "Hard-boiled egg with cherry tomatoes"
        ]
    }

    df_meal_plan = pd.DataFrame(meal_plan)
    st.table(df_meal_plan)

    # Calorie Calculator
    st.subheader("Calorie Calculator")
    calorie_data = {
        "Food Item": ["Grilled Chicken Breast", "Brown Rice", "Salmon", "Broccoli", "Sweet Potato", "Quinoa", "Greek Yogurt", "Almonds", "Avocado", "Banana", "Olive Oil", "Whole Grain Bread", "Egg"],
        "Serving Size": ["100g", "1/2 cup cooked", "100g", "1 cup", "1 medium", "1/2 cup cooked", "1 cup", "1 oz (23 almonds)", "1/2 medium", "1 medium", "1 tbsp", "1 slice", "1 large"],
        "Calories": [165, 108, 208, 31, 112, 111, 130, 164, 161, 105, 119, 69, 78]
    }

    df_calories = pd.DataFrame(calorie_data)
    st.table(df_calories)

    st.markdown("Note: These are approximate values. Actual calories may vary slightly based on specific brands and preparation methods.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Weekly Notes
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    st.header("Weekly Insights")
    weekly_notes = {
        1: "Started the program. Feeling motivated but challenged. Focus on gentle exercises and establishing a routine.",
        2: "Improved energy levels. Core exercises are getting easier. Introduced more walking and light strength training."
    }
    st.write(weekly_notes.get(selected_week, "No notes available for this week."))

    # Motivation Quote
    st.markdown('<div style="background-color: black; color: white; padding: 10px; border-radius: 5px;">"Small steps every day lead to big changes over time." - Jay Jung</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

show_karin_page()