import streamlit as st
import custom
import time

# Page configuration
st.set_page_config(page_title="Todo App", page_icon="📝", layout="centered")

# Custom CSS for a modern look
st.markdown("""
    <style>
    .main .block-container { max-width: 600px; padding-top: 2rem; }
    .stCheckbox { background-color: #f9f9f9; padding: 10px; border-radius: 5px; }
    </style>
""", unsafe_allow_html=True)

st.title("📝 Modern Todo App")
st.markdown("Manage and edit your daily tasks seamlessly.")

current_time = time.strftime("%b %d, %Y %H:%M:%S")
st.write(f"🗓️ It is {current_time}")
st.divider()


# Load tasks
todos = custom.get_todos()

# Function to add a todo
def add_todo():
    new_todo = st.session_state["new_todo"].strip()
    if new_todo:
        todos.append(new_todo + "\n")
        custom.write_todos(todos)
        st.session_state["new_todo"] = ""

def save_todo(index):
    updated_todo = st.session_state[f"edit_{index}"].strip()
    if updated_todo:
        todos[index] = updated_todo + "\n"
        custom.write_todos(todos)
        st.session_state[f"show_input_{index}"] = False  # Hide edit field

# 3. Read Current Tasks
todos = custom.get_todos()

# 4. Input Field to Add New Tasks
st.text_input(label="Add new todo:", placeholder="Type here...", on_change=add_todo, key="new_todo")
st.write("")

# 5. Display the Todo List
to_remove = None

for index, todo in enumerate(todos):
    clean_todo = todo.strip()
    
    # Create two columns: one for the checkbox, one for the edit button
    col1, col2 = st.columns([0.8, 0.2])
    
    with col1:
        if st.checkbox(clean_todo, key=f"check_{index}"):
            to_remove = index
            
    with col2:
        if st.button("✏️ Edit", key=f"btn_{index}"):
            st.session_state[f"show_input_{index}"] = True

    # If the user clicked "Edit", show the input field AND a Cancel button
    if st.session_state.get(f"show_input_{index}", False):
        # Create columns inside the edit view: 80% for input, 20% for cancel button
        edit_col1, edit_col2 = st.columns([0.8, 0.2])
        
        with edit_col1:
            st.text_input(
                label="Edit task (Press Enter to Save):",
                value=clean_todo,
                key=f"edit_{index}",
                on_change=save_todo,
                args=(index,)
            )
            
        with edit_col2:
            st.write("")  # Empty space to align the button vertically with the text input
            st.write("")
            if st.button("Cancel", key=f"cancel_{index}"):
                st.session_state[f"show_input_{index}"] = False  # Hide edit field
                st.rerun()  # Refresh the page instantly to clear the input box

# 6. Delete Task Safely
if to_remove is not None:
    todos.pop(to_remove)
    custom.write_todos(todos)
    st.rerun()