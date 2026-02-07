import streamlit as st
from agents.compressor_agent import compress_health_data
from agents.recommendation_agent import recommend_health

st.set_page_config(
    page_title="Personal Health Coach AI",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 Personal Health Coach AI")
st.write("Describe your daily health status and get instant insights & recommendations.")

st.divider()

user_input = st.text_area(
    "💬 Describe your health (sleep, stress, activity):",
    placeholder="Example: I feel tired, slept 5 hours, very stressed"
)

if st.button("🔍 Analyze Health"):
    if user_input.strip() == "":
        st.warning("Please enter your health details.")
    else:
        compressed_memory = compress_health_data(user_input)

        st.subheader("🧠 Compressed Health Memory")
        st.success(compressed_memory)

        st.subheader("💡 Health Recommendation")
        st.info(recommend_health(compressed_memory))

st.divider()
st.caption("🚀 Build in Public | Python Project | Health Coach AI")
