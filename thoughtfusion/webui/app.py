from functools import partial

import openai
import streamlit as st
from openai.error import AuthenticationError

from thoughtfusion.webui.chat import stream_chat
from thoughtfusion.webui.config import sidebar
from thoughtfusion.webui.prompts import (
    get_critic_prompt,
    get_system_prompt_messages,
    get_reasoning_questions_prompt,
)


def app():
    """Main Streamlit app"""
    st.set_page_config(
        page_title="ThoughtFusion", page_icon="🤖", layout="wide", initial_sidebar_state="collapsed"
    )

    st.title("ThoughtFusion")
    st.markdown(
        "ThoughtFusion uses two agents talking approach to answer your question. It's"
        " inspired by [Language Models can Solve Computer Tasks]"
        "(https://arxiv.org/abs/2303.17491) paper and similar works."
    )

    try:
        sidebar()
    except AuthenticationError:
        st.error("Invalid OpenAI API Key")
        return

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "critic_messages" not in st.session_state:
        st.session_state.critic_messages = []

    left, right = st.columns([0.5, 0.5])
    display_messages_history(left, st.session_state.messages)
    display_messages_history(right, st.session_state.critic_messages, critic=True)

    if "first_question" not in st.session_state:
        st.session_state.first_question = True

    if question := st.chat_input("Enter your question"):
        if st.session_state.first_question:
            if st.session_state.identify_personas:
                ai_persona, critic_persona = get_personas(
                    left, right, get_system_prompt_messages(question)
                )
                st.session_state.messages.append(
                    {"role": "system", "content": f"""You are {ai_persona}."""}
                )
                st.session_state.critic_messages.append(
                    {
                        "role": "system",
                        "content": f"""You are {critic_persona}. Your are tasked with analyzing answers and reviewing them, finding any potential problems or issues.""",
                    }
                )

            st.session_state.first_question = False

        for i in range(st.session_state.iterations):
            response = discuss(
                left,
                question,
                st.session_state.messages,
            )
            if i == 0:
                response = partial(get_reasoning_questions, question, response)
            question = discuss(
                right, response, st.session_state.critic_messages, avatar="🤖", ai_avatar="🧠"
            )
            if "ALL GOOD" in question:
                break


def display_messages_history(column, messages, critic=False):
    """Display messages in a column"""
    # Display chat messages from history on app rerun
    for message in messages:
        avatar = None
        if critic:
            if message["role"] == "user":
                avatar = "🤖"
            else:
                avatar = "🧠"
        if message["role"] == "system":
            avatar = "⚙️"
        with column.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])


def discuss(column, message, messages_history, *, avatar=None, ai_avatar=None):
    """Discuss with a chat"""
    with column.chat_message("user", avatar=avatar):
        # if message is callable
        if callable(message):
            message = message()
        else:
            st.markdown(message)

    messages_history.append({"role": "user", "content": message})

    with column.chat_message("assistant", avatar=ai_avatar):
        full_response = stream_chat(messages_history)

    messages_history.append({"role": "assistant", "content": full_response})
    return full_response


def get_personas(left, right, messages):
    """Get personas for system message"""
    left = left.chat_message("system", avatar="🤖")
    right = right.chat_message("system", avatar="🤖")

    placeholder = left.empty()
    full_response = ai_persona = ""
    for response in openai.ChatCompletion.create(
        model=st.session_state["openai_model"],
        messages=messages,
        stream=True,
    ):
        token = response.choices[0].delta.get("content", "")
        full_response += token
        placeholder.markdown(full_response + "▌")
        if token.endswith("\n"):
            placeholder.markdown(full_response)
            ai_persona = full_response
            placeholder = right.empty()
            full_response = ""
    placeholder.markdown(full_response)

    return ai_persona, full_response


def get_reasoning_questions(question, response):
    """Get reasoning questions"""
    critic_prompt_part1, critic_prompt_part2 = get_critic_prompt(
        question=question, response=response
    )
    st.markdown(critic_prompt_part1)

    reasoning_questions = stream_chat(get_reasoning_questions_prompt(question))
    st.markdown(critic_prompt_part2)
    return f"{critic_prompt_part1}{reasoning_questions}{critic_prompt_part2}"


if __name__ == "__main__":
    app()
