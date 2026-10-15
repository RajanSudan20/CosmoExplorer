import streamlit as st

# Page Configuration
st.set_page_config(page_title="Junior Astronaut Mission Trainer", page_icon="🚀", layout="wide")

# App Header
st.title("🚀 Junior Astronaut Mission Trainer")
st.markdown("Welcome to the **NASA Space Apps** training portal! Choose a destination to start your training.")

# Sidebar Selection
st.sidebar.header("🌌 Mission Control")
destination = st.sidebar.selectbox(
    "Choose Destination:",
    ["Mars (The Red Planet)", "Jupiter (Gas Giant)", "James Webb Space Telescope"]
)

# Content Display
if destination == "Mars (The Red Planet)":
    st.header("🔴 Mars: The Red Planet")
    st.image("https://images.unsplash.com/photo-1614728894747-a83421e2b9c9?q=80&w=1000&auto=format&fit=crop", width=700, caption="NASA Mars View")
    st.write("""
    * **Distance from Sun:** ~227.9 million km
    * **Gravity:** 3.721 m/s² (38% of Earth)
    * **Fun Fact:** Mars has Olympus Mons, the largest volcano in the solar system!
    """)
    
    # Quick Quiz
    st.subheader("👨‍🚀 Quick Cadet Check")
    ans = st.radio("What is the nickname of Mars?", ["The Blue Planet", "The Red Planet", "The Ringed Planet"])
    if st.button("Submit Answer"):
        if ans == "The Red Planet":
            st.success("Correct! Great job, Cadet! ⭐")
        else:
            st.error("Incorrect! Try again.")

elif destination == "Jupiter (Gas Giant)":
    st.header("🪐 Jupiter: The King of Planets")
    st.write("""
    * **Type:** Gas Giant
    * **Notable Feature:** The Great Red Spot (a massive storm bigger than Earth).
    """)

else:
    st.header("🔭 James Webb Space Telescope")
    st.write("""
    * **Mission:** Looking back in time at the earliest galaxies using infrared light.
    """)

# Footer
st.sidebar.markdown("---")
st.sidebar.info("Built by Team CosmoExplorer for NASA Space Apps 2026")
