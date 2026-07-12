import streamlit as st

def settings_page():

    st.title("⚙ Settings")

    st.write("Customize your LearnMate AI experience.")

    theme = st.selectbox(
        "Theme",
        [
            "Light",
            "Dark"
        ]
    )

    font = st.selectbox(
        "Font Size",
        [
            "Small",
            "Medium",
            "Large"
        ]
    )

    if st.button("Save Settings"):

        st.success("Settings saved successfully.")