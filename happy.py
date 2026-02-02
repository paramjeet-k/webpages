import streamlit as st
import random

st.set_page_config(
    page_title="Valentine 💖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# State
if "no_clicks" not in st.session_state:
    st.session_state.no_clicks = 0

# ---------- STYLE ----------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}

.card {
    background: #ffffff;
    padding: 35px;
    border-radius: 25px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.3);
    text-align: center;
    max-width: 420px;
    margin: auto;
}

.big-yes button {
    width: 100% !important;
    height: 70px !important;
    font-size: 28px !important;
    border-radius: 40px !important;
    background-color: #ff4d6d !important;
    color: white !important;
}

.small-no button {
    font-size: 14px !important;
    border-radius: 20px !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- CARD ----------
st.markdown("<div class='card'>", unsafe_allow_html=True)

# IMAGE (YES, YOU CAN ADD IMAGES ✅)
st.image(
    "https://i.imgur.com/4M7IWwP.png",  # cute cat image
    width=120
)

st.markdown("## 💖 Aastha Anand")
st.markdown("### Will you be my Valentine? 🌹")

st.write("")

# RANDOM BUTTON POSITION EFFECT
cols = st.columns(random.choice([3, 4, 5]))

# YES button (BIG)
with cols[0]:
    st.markdown("<div class='big-yes'>", unsafe_allow_html=True)
    if st.button("💖 YES 💖"):
        st.success("Yay! 💕 You just made my day 😍")
        st.balloons()
        st.stop()
    st.markdown("</div>", unsafe_allow_html=True)

# NO button (small + escaping)
with cols[-1]:
    st.markdown("<div class='small-no'>", unsafe_allow_html=True)
    if st.button("No 🙈"):
        st.session_state.no_clicks += 1
        st.warning(f"No is shy 😄 (tries: {st.session_state.no_clicks})")
        st.experimental_rerun()
    st.markdown("</div>", unsafe_allow_html=True)

st.caption("Hint: The NO button is very shy 😉")

st.markdown("</div>", unsafe_allow_html=True)
