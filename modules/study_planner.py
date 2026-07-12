import streamlit as st

from prompts.study_planner import study_plan_prompt
from services.gemini_service import generate_response


def study_planner_page():

    st.title("📅 AI Study Planner")

    topic = st.text_input("Topic")

    level = st.selectbox(
        "Difficulty",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    days = st.slider(
        "Number of Days",
        1,
        60,
        14
    )

    hours = st.slider(
        "Hours Per Day",
        1,
        10,
        2
    )

    if st.button(
        "Generate Study Plan",
        use_container_width=True
    ):

        if topic == "":
            st.warning("Enter topic")
            return

        with st.spinner("Creating Study Plan..."):

            prompt = study_plan_prompt(
                topic,
                level,
                days,
                hours
            )

            answer = generate_response(prompt)

        st.markdown(answer)