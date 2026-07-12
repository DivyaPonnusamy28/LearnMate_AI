import streamlit as st

from config import *

from prompts.explain import explain_prompt
from prompts.example import example_prompt
from prompts.feedback import feedback_prompt
from prompts.session import session_prompt
from prompts.study_notes import study_notes_prompt

from services.gemini_service import generate_response
from utils.history_manager import save_history


def learn_page():

    st.title("📘 Learn with AI")

    st.write("Choose a topic and let LearnMate AI teach you.")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        topic = st.text_input(
            "Topic",
            placeholder="Example: Artificial Intelligence"
        )

        difficulty = st.selectbox(
            "Difficulty",
            DIFFICULTY_LEVELS
        )

    with col2:

        activity = st.selectbox(
            "Activity",
            ACTIVITIES
        )

        student_answer = ""

        if activity == "Evaluate My Answer":

            student_answer = st.text_area(
                "Enter your answer"
            )

    generate = st.button(
        "🚀 Generate Response",
        use_container_width=True
    )

    if generate:

        if topic.strip() == "":
            st.warning("Please enter a topic.")
            return

        if activity == "Explain Concept":

            prompt = explain_prompt(
                topic,
                difficulty
            )

        elif activity == "Real-Life Example":

            prompt = example_prompt(
                topic,
                difficulty
            )

        elif activity == "Study Notes":

            prompt = study_notes_prompt(
                topic,
                difficulty
            )

        elif activity == "Evaluate My Answer":

            if student_answer.strip() == "":
                st.warning("Please enter your answer.")
                return

            prompt = feedback_prompt(
                topic,
                student_answer
            )

        elif activity == "Learning Tips":

            prompt = f"""
Give practical learning tips for mastering {topic}.
"""

        elif activity == "Interview Questions":

            prompt = f"""
Generate 10 interview questions with answers on {topic}.
"""

        elif activity == "Career Applications":

            prompt = f"""
Explain the career applications of {topic}.
"""

        else:

            prompt = session_prompt(
                topic,
                difficulty
            )

        with st.spinner("Thinking..."):

            answer = generate_response(prompt)

        save_history(
            topic,
            activity,
            difficulty,
            answer
        )

        st.divider()

        st.subheader("🤖 AI Response")

        with st.container(border=True):

            tab1, tab2 = st.tabs(
                [
                    "📄 Response",
                    "📋 Raw"
                ]
            )

            with tab1:

                st.markdown(answer)

            with tab2:

                st.code(answer)

        st.download_button(
            "📄 Download Response",
            answer,
            file_name="learnmate_response.txt"
        )