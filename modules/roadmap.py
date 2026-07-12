import streamlit as st

from prompts.roadmap import roadmap_prompt
from services.gemini_service import generate_response


def roadmap_page():

    st.title("🗺 AI Learning Roadmap")

    topic = st.text_input(
        "Enter a Topic"
    )

    level = st.selectbox(
        "Difficulty",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    if st.button(
        "Generate Roadmap",
        use_container_width=True
    ):

        if topic == "":

            st.warning("Enter a topic")

            return

        with st.spinner("Generating Roadmap..."):

            prompt = roadmap_prompt(
                topic,
                level
            )

            answer = generate_response(prompt)

        st.markdown(answer)