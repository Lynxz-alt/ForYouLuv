import streamlit as st

st.set_page_config(
    page_title="Happy Birthday, Luvi Hana Margareta 🌸",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
  #MainMenu, footer, header, .stDeployButton { visibility: hidden !important; }
  .block-container { padding: 0 !important; max-width: 100% !important; }
  [data-testid="stAppViewContainer"] { padding: 0 !important; }
  [data-testid="stVerticalBlock"] { gap: 0 !important; padding: 0 !important; }
  iframe { border: none !important; display: block !important; }
</style>
""", unsafe_allow_html=True)

with open("luvi_birthday.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=950, scrolling=False)
