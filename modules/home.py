import streamlit as st


def feature_card(title, desc, emoji, page):

    with st.container(border=True):

        st.markdown(f"""
        ## {emoji} {title}

        {desc}
        """)

        if st.button(
            f"Open {title}",
            key=page,
            use_container_width=True
        ):
            st.session_state.page = page
            st.rerun()


def home_page():

    if "user_email" in st.session_state:
        name = st.session_state.user_email.split("@")[0].title()
    else:
        name = "Learner"

    st.write(f"# 👋 Welcome back, {name}")

    st.markdown("""
    <div style="
        background:linear-gradient(135deg,#2563EB,#7C3AED);
        padding:40px;
        border-radius:20px;
        color:white;
        text-align:center;
        margin-bottom:20px;
    ">

    <h1>🎓 LearnMate AI</h1>

    <h3>Your Personalized AI Learning Companion</h3>

    <p>Learn • Practice • Revise • Grow</p>

    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("📘 Topics Learned", "15")
    c2.metric("📝 Quizzes", "8")
    c3.metric("🧠 Flashcards", "42")
    c4.metric("⏰ Study Hours", "28")

    st.divider()

    st.subheader("🚀 AI Learning Tools")

    left, right = st.columns(2)

    with left:

        feature_card(
            "Learn",
            "Explain any topic using AI.",
            "📘",
            "Learn"
        )

        feature_card(
            "Quiz",
            "Practice AI-generated quizzes.",
            "📝",
            "Quiz"
        )

    with right:

        feature_card(
            "Flashcards",
            "Generate revision flashcards.",
            "🧠",
            "Flashcards"
        )

        feature_card(
            "Learning Roadmap",
            "Step-by-step learning path.",
            "🗺",
            "Learning Roadmap"
        )

    st.divider()

    st.subheader("⭐ Today's Recommendation")

    st.success("""
Continue learning **Generative AI**

Recommended order

✅ Prompt Engineering

⬜ RAG

⬜ AI Agents

⬜ MCP

⬜ Fine-tuning
""")

    st.divider()

    st.info(
        "💡 Tip: Learn one AI concept every day for consistent progress."
    )