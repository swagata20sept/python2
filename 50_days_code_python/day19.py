# web app.............
import streamlit as st
import funcions
todos=funcions.get_todos()
def add_todo():
    todo=st.session_state["new_todo"]+ "\n"
    todos.append(todo)
    funcions.write_todos(todos)
st.title("My ToDo Application..")
st.subheader("This is my todo app...")
st.write("This app is to increase your productivity..")
for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        funcions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
st.text_input(label="",placeholder="add new todo...",on_change=add_todo,key="new_todo")
print("hiii..")