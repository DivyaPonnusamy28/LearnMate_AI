import streamlit as st

def show_header():

    col1, col2 = st.columns([1, 5])

    with col1:
        st.markdown("# 🎓")

    with col2:
        st.title("LearnMate AI")
        st.write("Your Personalized AI Learning Buddy powered by Gemini")

    st.divider()