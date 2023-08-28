import openai
import streamlit as st


def stream_chat(messages_history) -> str:
    """Stream a chat response"""
    message_placeholder = st.empty()
    full_response = ""
    for response in openai.ChatCompletion.create(
        model=st.session_state["openai_model"],
        messages=messages_history,
        stream=True,
    ):
        full_response += response.choices[0].delta.get("content", "")
        message_placeholder.markdown(full_response + "▌")
    message_placeholder.markdown(full_response)
    return full_response
