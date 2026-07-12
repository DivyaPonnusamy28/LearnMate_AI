import streamlit as st

def login_page():

    st.markdown(
        """
        <style>
        .title{
            text-align:center;
            font-size:52px;
            font-weight:700;
            color:#2563EB;
        }

        .subtitle{
            text-align:center;
            color:#666;
            font-size:20px;
            margin-bottom:25px;
        }

        div[data-testid="stForm"]{
            background:white;
            padding:35px;
            border-radius:18px;
            box-shadow:0px 10px 30px rgba(0,0,0,.15);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="title">🎓 LearnMate AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Your Personalized AI Learning Companion</div>',
        unsafe_allow_html=True
    )

    left, center, right = st.columns([1,2,1])

    with center:

        with st.form("login"):

            email = st.text_input("📧 Email")

            password = st.text_input(
                "🔒 Password",
                type="password"
            )

            login = st.form_submit_button(
                "Login",
                use_container_width=True
            )

            if login:

                if email == "" or password == "":
                    st.error("Enter Email and Password.")

                else:
                    st.session_state.logged_in = True
                    st.session_state.user_email = email
                    st.session_state.page = "Home"
                    st.rerun()