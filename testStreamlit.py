import streamlit as st
from datetime import datetime
import pytz
import time

st.title("ΚΑΛΩΣ ΗΡΘΑΤΕ ΣΤΟ PORTAL ΤΩΝ ΚΑΘΥΣΤΕΡΗΜΕΝΩΝ")

athens_tz = pytz.timezone("Europe/Athens")
current_time = datetime.now(athens_tz).strftime("%H:%M:%S")

st.write(f"Current time in Athens: {current_time}")
