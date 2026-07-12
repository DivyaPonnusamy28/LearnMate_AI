import streamlit as st

def stats_cards():

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Activities",
            "8"
        )

    with c2:
        st.metric(
            "AI Model",
            "Gemini"
        )

    with c3:
        st.metric(
            "Difficulty",
            "3 Levels"
        )


def feature_cards():

    st.markdown("## ✨ Features")

    a, b, c = st.columns(3)

    with a:
        st.success("""
📚 Study Notes

Generate complete notes instantly.
""")

    with b:
        st.info("""
🧠 Flashcards

Revise quickly with AI flashcards.
""")

    with c:
        st.warning("""
📄 PDF Export

Download your learning notes.
""")