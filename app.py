import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="CosmoExplorer - 3D Space Map", page_icon="🚀", layout="wide")

# Custom dark space theme styling
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: white; }
    </style>
""", unsafe_allow_html=True)

st.title("🌌 CosmoExplorer: Interactive 3D Deep Space Map")
st.markdown("Mission Control v2.0 - Real-time celestial coordinate mapping inspired by NASA telemetry.")

# Enhanced space data with realistic positioning
space_data = {
    'Object': ['Sun (Sol)', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Deep Space Nebula'],
    'X': [0, 0.4, 0.7, 1.0, 1.5, 5.2, 9.5, 20.0],
    'Y': [0, 0.2, 0.5, 0.8, 1.2, 4.0, 8.0, 18.0],
    'Z': [0, 0.1, 0.3, 0.6, 1.0, 3.5, 7.0, 15.0],
    'Size': [80, 15, 22, 25, 22, 50, 45, 70],
    'Type': ['Star', 'Planet', 'Planet', 'Habitable', 'Planet', 'Gas Giant', 'Gas Giant', 'Nebula']
}

df = pd.DataFrame(space_data)

# 3D Plotly Map with game-like space aesthetics (no grid lines)
fig = px.scatter_3d(
    df, x='X', y='Y', z='Z',
    size='Size',
    color='Type',
    hover_name='Object',
    text='Object',
    title="Live 3D Celestial Matrix"
)

# Removing grid lines and background to make it look like deep space
fig.update_layout(
    scene=dict(
        xaxis=dict(showbackground=False, showgrid=False, zeroline=False, showticklabels=False, title=''),
        yaxis=dict(showbackground=False, showgrid=False, zeroline=False, showticklabels=False, title=''),
        zaxis=dict(showbackground=False, showgrid=False, zeroline=False, showticklabels=False, title=''),
        bgcolor='#050505'
    ),
    paper_bgcolor='#050505',
    font=dict(color='white'),
    showlegend=True,
    height=600
)

st.plotly_chart(fig, use_container_width=True)

# Interactive Telemetry Inspection Panel
st.markdown("---")
st.subheader("🔭 Selected Mission Target Telemetry")
selected_obj = st.selectbox("Choose a celestial body to inspect:", df['Object'].tolist())

if selected_obj == "Earth":
    st.info("🌍 **Earth**: Our home planet. Rich in liquid water, oxygen-nitrogen atmosphere, and complex life supporting ecosystems.")
elif selected_obj == "Mars":
    st.warning("🔴 **Mars**: The Red Planet. Features massive canyons like Valles Marineris and Olympus Mons, the tallest volcano.")
elif selected_obj == "Sun (Sol)":
    st.error("☀️ **Sun**: The center of our solar system, driving gravitational orbits and solar space weather.")
else:
    st.success(f"✨ **{selected_obj}**: Deep space anomaly or outer body tracked by NASA telemetry systems.")
