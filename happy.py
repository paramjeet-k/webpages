import streamlit as st
import random

st.set_page_config(page_title="Valentine 💖", layout="centered")

# Session state to track No clicks
if "no_clicks" not in st.session_state:
    st.session_state.no_clicks = 0

st.markdown(
    """
    <style>
    .card {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 15px 30px rgba(0,0,0,0.15);
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown("## 🐱💖")
st.markdown("### Nirali, will you be my Valentine?")

# Random layout for buttons
cols = st.columns(random.choice([2, 3, 4]))

yes_col = cols[0]
no_col = cols[-1]

with yes_col:
    if st.button("💖 Yes"):
        st.success("Yay! 💖 You just made my day 😍")
        st.balloons()
        st.stop()

with no_col:
    if st.button("🙈 No"):
        st.session_state.no_clicks += 1
        st.warning(f"Nice try 😄  No is feeling shy ({st.session_state.no_clicks})")
        st.experimental_rerun()

st.caption("Hint: The 'No' button is very shy 😄")

st.markdown("</div>", unsafe_allow_html=True)
