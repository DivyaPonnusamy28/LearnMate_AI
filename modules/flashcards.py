import streamlit as st
import json

from prompts.flashcards_prompt import flashcards_prompt
from services.gemini_service import generate_response


def flashcards_page():

    st.title("🃏 AI Flashcards")

    # -------------------------
    # Session State
    # -------------------------

    if "flashcards" not in st.session_state:
        st.session_state.flashcards = []

    if "card_index" not in st.session_state:
        st.session_state.card_index = 0

    if "show_answer" not in st.session_state:
        st.session_state.show_answer = False

    # -------------------------
    # Input
    # -------------------------

    topic = st.text_input(
        "Enter Topic"
    )

    difficulty = st.selectbox(
        "Difficulty",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    # -------------------------
    # Generate Flashcards
    # -------------------------

    if st.button(
        "Generate Flashcards",
        use_container_width=True
    ):

        if topic.strip() == "":
            st.warning("Please enter a topic.")
            return

        with st.spinner("Creating Flashcards..."):

            prompt = flashcards_prompt(
                topic,
                difficulty
            )

            response = generate_response(prompt)

            response = response.replace("```json", "")
            response = response.replace("```", "")
            response = response.strip()

            try:

                cards = json.loads(response)

                st.session_state.flashcards = cards
                st.session_state.card_index = 0
                st.session_state.show_answer = False

                st.success("Flashcards Generated!")

            except Exception:

                st.error("Invalid JSON returned.")

                st.code(response)

                return

    # -------------------------
    # Stop if no flashcards
    # -------------------------

    if len(st.session_state.flashcards) == 0:
        return

    cards = st.session_state.flashcards
    index = st.session_state.card_index

    card = cards[index]

    st.divider()

    st.progress((index + 1) / len(cards))

    st.markdown(
        f"### Card {index+1} of {len(cards)}"
    )

    st.markdown("---")

    st.markdown("## ❓ Question")

    st.info(card["question"])

    if st.button(
        "👀 Show Answer",
        key="answer"
    ):
        st.session_state.show_answer = True

    if st.session_state.show_answer:

        st.success(card["answer"])

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "⬅ Previous",
            use_container_width=True
        ):

            if index > 0:

                st.session_state.card_index -= 1
                st.session_state.show_answer = False

                st.rerun()

    with col2:

        if st.button(
            "Next ➡",
            use_container_width=True
        ):

            if index < len(cards) - 1:

                st.session_state.card_index += 1
                st.session_state.show_answer = False

                st.rerun()

    st.divider()

    st.caption(
        "💡 Tip: Read the question first, think of the answer, then reveal it."
    )