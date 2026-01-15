import streamlit as st
import random
from streamlit_javascript import st_javascript

st.title("🐍 Snake Game")

# Capture keyboard input
key = st_javascript("""
    new Promise((resolve) => {
        document.addEventListener('keydown', function handler(e) {
            if(['ArrowUp','ArrowDown','ArrowLeft','ArrowRight'].includes(e.key)) {
                document.removeEventListener('keydown', handler);
                resolve(e.key);
            }
        });
    })
""")

# Initialize game state
if "snake" not in st.session_state:
    st.session_state.snake = [(5, 5)]
    st.session_state.food = (random.randint(0, 9), random.randint(0, 9))
    st.session_state.score = 0
    st.session_state.game_over = False

# Process key press
if key and not st.session_state.game_over:
    head = st.session_state.snake[0]
    if key == "ArrowUp":
        new_head = (head[0], head[1] - 1)
    elif key == "ArrowDown":
        new_head = (head[0], head[1] + 1)
    elif key == "ArrowLeft":
        new_head = (head[0] - 1, head[1])
    elif key == "ArrowRight":
        new_head = (head[0] + 1, head[1])
    
    if new_head[0] < 0 or new_head[0] > 9 or new_head[1] < 0 or new_head[1] > 9:
        st.session_state.game_over = True
    elif new_head in st.session_state.snake:
        st.session_state.game_over = True
    else:
        st.session_state.snake.insert(0, new_head)
        if new_head == st.session_state.food:
            st.session_state.score += 1
            st.session_state.food = (random.randint(0, 9), random.randint(0, 9))
        else:
            st.session_state.snake.pop()

# Draw grid
grid = ""
for y in range(10):
    for x in range(10):
        if (x, y) in st.session_state.snake:
            grid += "🟩"
        elif (x, y) == st.session_state.food:
            grid += "🍎"
        else:
            grid += "⬛"
    grid += "\n"

st.text(grid)
st.write(f"Score: {st.session_state.score}")

if st.session_state.game_over:
    st.error("Game Over!")
    if st.button("Restart"):
        st.session_state.snake = [(5, 5)]
        st.session_state.food = (random.randint(0, 9), random.randint(0, 9))
        st.session_state.score = 0
        st.session_state.game_over = False
        st.rerun()

