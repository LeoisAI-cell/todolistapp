import streamlit as st

st.title("To-Do List")

if 'tasks' not in st.session_state:
    st.session_state.tasks = []

task = st.text_input("Enter a new task:")

if st.button("Add Task"):
    st.session_state.tasks.append(task)

if st.button("Clear All Tasks"):
    st.session_state.tasks.clear()

st.write("Your Tasks:")
for i, task in enumerate(st.session_state.tasks):
    st.write(f"{i+1}. {task}")
