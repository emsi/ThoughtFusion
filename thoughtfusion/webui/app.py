import streamlit as st
from openai.error import AuthenticationError

from thoughtfusion.webui.config import sidebar


def app():
    """Main Streamlit app"""
    st.set_page_config(page_title="ThoughtFusion", page_icon="🤖", layout="wide")

    st.title("ThoughtFusion")
    st.markdown("")

    try:
        sidebar()
    except AuthenticationError:
        st.error("Invalid OpenAI API Key")
        return

    user_question = st.text_input("Enter your question")

    left, right = st.columns([0.5, 0.5])

    with left.chat_message("assistant"):
        st.write("OO")

    with right.chat_message("ai"):
        st.write("OO")



if __name__ == "__main__":
    app()
