import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("Meine Todo App")
st.subheader('Das ist meine Todo App')
st.write('Diese App dient als kleine Gedächtnisstütze im Alltag')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="ToDo-Eingabe:", placeholder="Todo-intragen...",
              on_change=add_todo, key='new_todo')
