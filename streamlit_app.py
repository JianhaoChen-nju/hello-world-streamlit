from pathlib import Path

import streamlit as st

st.set_page_config(page_title="你好，世界 · 世界的一角", page_icon="🌍", layout="wide")
st.iframe(
    Path(__file__).with_name("index.html"),
    height="content",
    width="stretch",
    alt="你好，世界：一个可以点击按钮收到问候的小站。",
)
