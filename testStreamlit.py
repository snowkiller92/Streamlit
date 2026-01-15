import streamlit as st
from datetime import datetime
import pytz
import time

st.title("Μπορώ να αφήσω τον υπολογιστή ανοιχτό για να μην χασω τα chat με το ChatGPT? δεν θελω να κανω account")

athens_tz = pytz.timezone("Europe/Athens")
current_time = datetime.now(athens_tz).strftime("%H:%M:%S")

st.write(f"Current time in Athens: {current_time}")


