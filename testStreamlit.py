import streamlit as st
import random

st.title("🐍 Snake Game")

# Initialize game state
if "snake" not in st.session_state:
    st.session_state.snake = [(5, 5)]
    st.session_state.food = (random.randint(0, 9), random.randint(0, 9))
    st.session_state.direction = "RIGHT"
    st.session_state.score = 0
    st.session_state.game_over = False

def move():
    if st.session_state.game_over:
        return
    head = st.session_state.snake[0]
    if st.session_state.direction == "UP":
        new_head = (head[0], head[1] - 1)
    elif st.session_state.direction == "DOWN":
        new_head = (head[0], head[1] + 1)
    elif st.session_state.direction == "LEFT":
        new_head = (head[0] - 1, head[1])
    else:
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

# Controls
st.write("**Controls:**")
col1, col2, col3 = st.columns([1,1,1])
with col2:
    if st.button("⬆️", use_container_width=True):
        st.session_state.direction = "UP"
        move()

col1, col2, col3 = st.columns([1,1,1])
with col1:
    if st.button("⬅️", use_container_width=True):
        st.session_state.direction = "LEFT"
        move()
with col2:
    if st.button("⬇️", use_container_width=True):
        st.session_state.direction = "DOWN"
        move()
with col3:
    if st.button("➡️", use_container_width=True):
        st.session_state.direction = "RIGHT"
        move()

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
st.write(f"**Score: {st.session_state.score}**")

if st.session_state.game_over:
    st.error("Game Over!")
    if st.button("🔄 Restart"):
        st.session_state.snake = [(5, 5)]
        st.session_state.food = (random.randint(0, 9), random.randint(0, 9))
        st.session_state.direction = "RIGHT"
        st.session_state.score = 0
        st.session_state.game_over = False
        st.rerun()
