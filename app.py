import streamlit as st

from components.sidebar import show_sidebar

from modules.login import login_page
from modules.home import home_page
from modules.learn import learn_page
from modules.quiz import quiz_page
from modules.flashcards import flashcards_page
from modules.notes import notes_page
from modules.roadmap import roadmap_page
from modules.study_planner import study_planner_page
from modules.history import history_page

st.set_page_config(
    page_title="LearnMate AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CSS ---------------- #

def load_css():
    with open("css/main.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# ---------------- Session ---------------- #

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "user_email" not in st.session_state:
    st.session_state.user_email = ""

# ---------------- Login ---------------- #

if not st.session_state.logged_in:
    login_page()
    st.stop()

# ---------------- Sidebar ---------------- #

show_sidebar()

page = st.session_state.page

# ---------------- Routing ---------------- #

if page == "Home":
    home_page()

elif page == "Learn":
    learn_page()

elif page == "Quiz":
    quiz_page()

elif page == "Flashcards":
    flashcards_page()

elif page == "Notes":
    notes_page()

elif page == "Learning Roadmap":
    roadmap_page()

elif page == "Study Planner":
    study_planner_page()

elif page == "History":
    history_page()