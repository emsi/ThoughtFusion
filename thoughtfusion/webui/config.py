import openai
import streamlit as st

from thoughtfusion.webui.secret import read_secret


def model_choose(*, model_prefix, default_model, session_name):
    """Select a model"""
    openai_models = openai.Model.list().data
    whisper_models = [
        model["id"] for model in openai_models if model["id"].startswith(model_prefix)
    ]

    st.session_state[session_name] = st.sidebar.selectbox(
        "Model",
        whisper_models,
        index=whisper_models.index(st.session_state.get(session_name, default_model)),
    )


def sidebar():
    """Configuration sidebar"""
    st.sidebar.title("🤖Options")

    openai.api_key = st.sidebar.text_input(
        "OpenAI API key",
        getattr(openai, "api_key") or read_secret("openai_api_key.txt"),
        type="password",
    )
    model_choose(model_prefix="gpt-", default_model="gpt-4", session_name="gpt_model")
    openai.organization = st.sidebar.text_input("OpenAI organization", openai.organization or "")
    st.session_state["manipulate_temperature"] = st.sidebar.slider(
        "Temperature", 0.0, 2.0, st.session_state.get("summary_temperature", 0.0)
    )