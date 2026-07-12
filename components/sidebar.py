import streamlit as st
from streamlit_option_menu import option_menu

def show_sidebar():

    selected = option_menu(

        menu_title=None,

        options=[
            "Home",
            "Learn",
            "Quiz",
            "Flashcards",
            "Notes",
            "Learning Roadmap",
            "Study Planner",
            "History"
        ],

        icons=[
            "house",
            "book",
            "patch-question",
            "layers",
            "journal-text",
            "map",
            "calendar",
            "clock-history"
        ],

        orientation="horizontal",

        default_index=0,

    )

    st.session_state.page = selected