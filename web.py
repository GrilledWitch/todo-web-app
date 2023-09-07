import streamlit as st
import functions as fc


def add_todo():
    new_todo = st.session_state["todo-input"]
    fc.append_data(new_todo)
    st.session_state["todo-input"] = ""


todos = fc.get_data()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    check_box = st.checkbox(todo, key=todo)
    if check_box:
        todos.pop(index)
        fc.write_data(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Todo", placeholder="Add new todo",
              on_change=add_todo, label_visibility="hidden",
              key="todo-input")
