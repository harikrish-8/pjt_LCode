import streamlit as st
from namelist import get_leaderboard

st.set_page_config(
    page_title="LeetTracker",
    page_icon="🐍",
    layout="wide"
)

st.title("🏆 LeetTracker Leaderboard")

df = get_leaderboard()

st.dataframe(df, use_container_width=True, hide_index=True)