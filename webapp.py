import streamlit as st
from streamlit import checkbox
import functions

tasks = functions.get_todos()

def add_task():
    task = st.session_state["input"] + '\n'
    tasks.append(task.capitalize())
    functions.write_todos(tasks)
    st.session_state["input"] = ""

st.title("My To-Do_App")
st.text_input(label = "Enter your task : ", on_change=add_task, key = "input")

for index, task in enumerate(tasks):
    checkbox = st.checkbox(task, key = task)
    if checkbox:
        tasks.pop(index)
        functions.write_todos(tasks)
        del st.session_state[task]
        st.rerun()

