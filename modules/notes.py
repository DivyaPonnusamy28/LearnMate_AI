import streamlit as st

from prompts.notes_prompt import notes_prompt
from services.gemini_service import generate_response


def notes_page():

    st.title("📝 AI Study Notes")

    topic = st.text_input("Topic")

    difficulty = st.selectbox(
        "Difficulty",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    if st.button(
        "Generate Notes",
        use_container_width=True
    ):

        if topic == "":
            st.warning("Enter Topic")
            return

        with st.spinner("Generating Notes..."):

            answer = generate_response(
                notes_prompt(
                    topic,
                    difficulty
                )
            )

        st.markdown(answer)

        st.download_button(
            "📄 Download Notes",
            answer,
            file_name=f"{topic}_notes.md"
        )