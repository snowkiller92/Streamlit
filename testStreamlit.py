import streamlit as st
from datetime import datetime
import pytz
import base64

# def check_password():
#     if "authenticated" not in st.session_state:
#         st.session_state.authenticated = False
    
#     if not st.session_state.authenticated:
#         st.title("🔒 Login")
#         password = st.text_input("Enter password:", type="password")
#         if st.button("Login"):
#             if password == "mypassword123":  # Change this
#                 st.session_state.authenticated = True
#                 st.rerun()
#             else:
#                 st.error("Wrong password")
#         return False
#     return True

# if not check_password():
#     st.stop()

# App starts here
st.title("ΝΟΟΤΡΟΠΙΑ, READ A BOOK")

st.image("gio.png", width=300)

athens_tz = pytz.timezone("Europe/Athens")
current_time = datetime.now(athens_tz).strftime("%H:%M:%S")

st.write(f"Current time in Athens: {current_time}")

col1, col2 = st.columns(2)

with col1:
    if st.button("Update Time"):
        st.rerun()

with col2:
    if st.button("▶️ ΔΩΡΕΑΝ ΜΟΡΦΩΣΗ"):
        with open("gio.mp3", "rb") as f:
            audio_bytes = f.read()
            audio_base64 = base64.b64encode(audio_bytes).decode()
            st.markdown(f'<audio autoplay><source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3"></audio>', unsafe_allow_html=True)


