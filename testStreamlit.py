import streamlit as st
from datetime import datetime
import pytz
import time

st.title("If you are reading this you are gay")

athens_tz = pytz.timezone("Europe/Athens")
current_time = datetime.now(athens_tz).strftime("%H:%M:%S")

st.write(f"Current time in Athens: {current_time}")




