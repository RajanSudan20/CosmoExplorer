import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Junior Astronaut Mission Trainer", page_icon="🚀", layout="wide")

st.title("🚀 Junior Astronaut Mission Trainer & 3D Cosmic Map")
st.markdown("Welcome to the **NASA Space Apps** training portal! Explore the 3D space map below.")

# Sample 3D Space Coordinates Data (Relative scale for visualization)
space_data = {
    'Celestial Object': ['Sun', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Deep Space Nebula'],
    'X_Axis': [0, 0.4, 0.7, 1.0, 1.5, 5.2, 9.5, 20.0],
    'Y_Axis': [0, 0.2, 0.5, 0.8, 1.2, 4.0, 8.0, 18.0],
    'Z_Axis': [0, 0.1, 0.3, 0.6, 1.0, 3.5, 7.0, 15.0],
    'Size': [60, 10, 15, 20, 18, 40, 35, 50],
    'Category': ['Star', 'Planet', 'Planet', 'Planet', 'Planet', 'Planet', 'Planet', 'Deep Space']
}

df = pd.DataFrame(space_data)

# Sidebar Control
st.sidebar.header("🌌 Navigation & Controls")
view_mode = st.sidebar.radio("Select View:", ["3D Cosmic Map", "Mission Quizzes"])

if view_mode == "3D Cosmic Map":
    st.subheader("🪐 Interactive 3D Universe & Solar System Map")
    st.write("Aap is 3D chart ko mouse se click karke kisi bhi direction mein rotate aur zoom kar sakte hain!")

    # Creating 3D Scatter Plot using Plotly
    fig = px.scatter_3d(
        df, 
        x='X_Axis', 
        y='Y_Axis', 
        z='Z_Axis', 
        size='Size', 
        color='Category',
        hover_name='Celestial Object',
        title="3D Space Explorer Matrix"
    )
    
    # Customizing layout for dark space theme look
    fig.update_layout(
        scene=dict(
            xaxis_backgroundcolor="black",
            yaxis_backgroundcolor="black",
            zaxis_backgroundcolor="black",
            bgcolor="black"
        ),
        paper_bgcolor="black",
        font_color="white"
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.subheader("🎯 Junior Astronaut Qualification Exam")
    ans = st.radio("Which planet has the largest volcano (Olympus Mons)?", ["Earth", "Mars", "Jupiter"])
    if st.button("Submit Answer"):
        if ans == "Mars":
            st.success("Correct! Great job, Cadet! ⭐")
        else:
            st.error("Incorrect! Try again.")
