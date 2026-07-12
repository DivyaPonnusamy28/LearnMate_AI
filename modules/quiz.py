import streamlit as st
import json

from prompts.quiz_json import quiz_json_prompt
from services.gemini_service import generate_response
from utils.storage import load_data, save_data


# ----------------------------
# Load CSS
# ----------------------------

def load_css():
    try:
        with open("css/quiz.css") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )
    except:
        pass


# ----------------------------
# Initialize
# ----------------------------

def initialize():

    defaults = {
        "quiz": None,
        "current_question": 0,
        "answers": {},
        "submitted": False,
        "score": 0
    }

    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


# ----------------------------
# Generate Quiz
# ----------------------------

def generate_quiz(topic, difficulty):

    prompt = quiz_json_prompt(topic, difficulty)

    response = generate_response(prompt)

    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    quiz = json.loads(response)

    st.session_state.quiz = quiz
    st.session_state.current_question = 0
    st.session_state.answers = {}
    st.session_state.submitted = False
    st.session_state.score = 0


# ----------------------------
# Quiz Page
# ----------------------------

def quiz_page():

    load_css()

    initialize()

    st.title("📝 Interactive AI Quiz")

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
        "Generate Quiz",
        use_container_width=True
    ):

        if topic == "":
            st.warning("Enter a topic.")
            st.stop()

        with st.spinner("Generating Quiz..."):
            generate_quiz(topic, difficulty)

    if st.session_state.quiz is None:
        return

    quiz = st.session_state.quiz

    total = len(quiz)

    current = st.session_state.current_question

    q = quiz[current]

    st.progress((current + 1) / total)

    st.markdown(
        f"### Question {current+1} of {total}"
    )

    st.write(q["question"])

    selected = st.radio(
        "",
        q["options"],
        key=f"question_{current}",
        index=None
    )

    if selected is not None:
        st.session_state.answers[current] = selected

    col1, col2, col3 = st.columns(3)

    with col1:

        if current > 0:

            if st.button("⬅ Previous"):

                st.session_state.current_question -= 1
                st.rerun()

    with col2:

        st.markdown(
            f"<center><b>{current+1}/{total}</b></center>",
            unsafe_allow_html=True
        )

    with col3:

        if current < total - 1:

            if st.button("Next ➡"):

                st.session_state.current_question += 1
                st.rerun()

    st.divider()

    if current == total - 1:

        if st.button(
            "✅ Submit Quiz",
            use_container_width=True
        ):

            score = 0

            for i, ques in enumerate(quiz):

                if i not in st.session_state.answers:
                    continue

                selected = st.session_state.answers[i]

                correct = ques["options"][ques["answer"]]

                if selected == correct:
                    score += 1


# --------------------
# Save Analytics
# --------------------

            data = load_data()

            data["quiz_scores"].append(score)

            data["topics"].append(topic)

            data["sessions"] += 1

            save_data(data)

# --------------------

            st.session_state.score = score
            st.session_state.submitted = True

            st.rerun()
    # --------------------
    # Result
    # --------------------

    if st.session_state.submitted:

        st.divider()

        st.header("📊 Result")

        score = st.session_state.score

        percentage = round(
            score / total * 100,
            2
        )

        st.metric(
            "Score",
            f"{score}/{total}"
        )

        st.progress(score / total)

        st.success(f"Accuracy : {percentage}%")

        if percentage == 100:

            st.success("🏆 Perfect Score!")

            st.markdown("# ✨✨✨ Congratulations! ✨✨✨")

        elif percentage >= 80:

            st.success("🌟 Excellent!")

        elif percentage >= 60:

            st.info("👍 Good Job!")

        else:

            st.warning("📚 Keep Practicing!")

        st.divider()

        st.header("Solutions")

        for i, ques in enumerate(quiz):

            st.markdown(f"### Q{i+1}")

            st.write(ques["question"])

            selected = st.session_state.answers.get(i, "Not Answered")

            correct = ques["options"][ques["answer"]]

            if selected == correct:

                st.success(f"✅ Your Answer : {selected}")

            else:

                st.error(f"❌ Your Answer : {selected}")

                st.success(f"✅ Correct : {correct}")

            st.info(ques["explanation"])

            st.divider()

        if st.button(
            "🔄 Retake Quiz",
            use_container_width=True
        ):

            st.session_state.quiz = None
            st.session_state.answers = {}
            st.session_state.current_question = 0
            st.session_state.submitted = False
            st.session_state.score = 0

            st.rerun()