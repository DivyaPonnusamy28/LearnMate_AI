import streamlit as st

from utils.history_manager import load_history


def history_page():

    st.title("📜 Learning History")

    history = load_history()

    if len(history) == 0:

        st.info("No learning history yet.")

        return

    for item in history:

        with st.expander(
            f"{item['topic']} • {item['activity']} • {item['time']}"
        ):

            st.write(f"Difficulty : {item['difficulty']}")

            st.divider()

            st.markdown(item["response"])