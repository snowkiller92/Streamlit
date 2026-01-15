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

if st.button("Refresh time"):
    st.rerun()

st.write("Δωρεάν Μόρφωση")  # Change this to whatever you want
st.audio("gio.mp3")


