import os
import streamlit as st
from dotenv import load_dotenv

# Load local .env (for local development)
load_dotenv()

# API Key
if "GEMINI_API_KEY" in st.secrets:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
else:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# App Details
APP_NAME = "LearnMate AI"
APP_ICON = "🎓"
APP_VERSION = "1.0"

# Difficulty Levels
DIFFICULTY_LEVELS = [
    "Beginner",
    "Intermediate",
    "Advanced"
]

# Activities
ACTIVITIES = [
    "Explain Concept",
    "Real-Life Example",
    "Study Notes",
    "Evaluate My Answer",
    "Learning Tips",
    "Interview Questions",
    "Career Applications",
    "Ask Anything"
]

RESPONSIBLE_AI = """
⚠ AI-generated responses may occasionally be incorrect.
Always verify important educational or technical information.
"""