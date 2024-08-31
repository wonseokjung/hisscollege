import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import importlib
import os

# Configuration
st.set_page_config(page_title="HISS COLLEGE Dashboard", layout="wide")

# Function to load student data from individual pages
def load_student_data(module_name):
    try:
        module = importlib.import_module(f"pages.{module_name}")
        if hasattr(module, 'get_student_data'):
            return module.get_student_data()
        else:
            st.warning(f"No get_student_data() function found in {module_name}")
    except Exception as e:
        st.error(f"Error loading data from {module_name}: {str(e)}")
    return None

# Data loading from individual student pages
@st.cache_data
def load_data():
    data_list = []
    for filename in os.listdir('pages'):
        if filename.endswith('.py'):
            module_name = filename[:-3]
            data = load_student_data(module_name)
            if data:
                data_list.append(data)
    return pd.DataFrame(data_list)

def main():
    st.title("🎓 HISS COLLEGE Interactive Dashboard")

    df = load_data()

    if df.empty:
        st.warning("No student data available. Please check your student data files.")
        return

    st.header("Student Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Students", len(df))
    col2.metric("Average Progress", f"{df['Progress'].mean():.1%}")
    col3.metric("Best Performer", df.loc[df['Performance'].idxmax(), 'Name'])

    st.subheader("Student Progress")
    fig = px.bar(df, x="Name", y="Progress", color="Major", text="Progress")
    fig.update_traces(texttemplate='%{text:.1%}', textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

    st.header("Student Details")
    selected_student = st.selectbox("Select a student", df['Name'])
    student_data = df[df['Name'] == selected_student].iloc[0]

    col1, col2 = st.columns(2)
    with col1:
        st.subheader(f"{selected_student}'s Progress")
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=student_data["Current Week"],
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Current Week", 'font': {'size': 24}},
            gauge={
                'axis': {'range': [None, student_data["Total Weeks"]], 'tickwidth': 1, 'tickcolor': "darkblue"},
                'bar': {'color': "darkblue"},
                'steps': [{'range': [0, student_data["Total Weeks"]], 'color': 'royalblue'}],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': student_data["Total Weeks"]}}))
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader(f"{selected_student}'s Performance")
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=student_data['Performance'],
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Performance Score"},
            gauge={
                'axis': {'range': [None, 100]},
                'steps': [
                    {'range': [0, 50], 'color': "lightgray"},
                    {'range': [50, 75], 'color': "gray"}],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 90}}))
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Student Information")
    st.json(student_data.to_dict())

if __name__ == "__main__":
    main()