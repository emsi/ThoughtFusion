import os
from typing import Optional

import streamlit as st


def _read_secret(secret_file_path: str) -> Optional[str]:
    if os.path.exists(secret_file_path):
        with open(secret_file_path, "r") as f:
            return f.read().strip()
    return ""


@st.cache_resource(show_spinner=f"Please wait.")
def read_secret(secret_file_path: str) -> Optional[str]:
    """
    Read a secret from file or request it from the user.

    :param secret_file_path: path to the file with the secret
    :return: secret
    """
    return _read_secret(secret_file_path)
