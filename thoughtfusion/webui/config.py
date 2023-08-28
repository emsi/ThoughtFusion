import openai
import streamlit as st

from thoughtfusion.webui.secret import read_secret


@st.cache_data(show_spinner=False)
def _model_choose(*, model_prefix):
    openai_models = openai.Model.list().data
    return [model["id"] for model in openai_models if model["id"].startswith(model_prefix)]


def model_choose(*, model_prefix, default_model, session_name):
    """Select a model"""
    whisper_models = _model_choose(model_prefix=model_prefix)
    st.session_state[session_name] = st.selectbox(
        "Model",
        whisper_models,
        index=whisper_models.index(st.session_state.get(session_name, default_model)),
    )


def sidebar():
    """Configuration sidebar"""
    st.sidebar.title("🤖Options")

    openai_expander = st.sidebar.expander("OpenAI API Settings")
    st.session_state.iterations = st.sidebar.slider(
        "Iterations", min_value=1, max_value=10, value=st.session_state.get("iterations", 3)
    )
    st.session_state.identify_personas = st.sidebar.checkbox(
        "Identify personas", st.session_state.get("identify_personas", True)
    )
    with openai_expander:
        openai.api_key = st.text_input(
            "OpenAI API key",
            getattr(openai, "api_key") or read_secret("openai_api_key.txt"),
            type="password",
        )
        model_choose(model_prefix="gpt-", default_model="gpt-4", session_name="openai_model")
        openai.organization = st.text_input("OpenAI organization", openai.organization or "")
        st.session_state["manipulate_temperature"] = st.slider(
            "Temperature", 0.0, 2.0, st.session_state.get("summary_temperature", 0.0)
        )
