
import streamlit as st
import requests

st.header("Task Management")

if "login" not in st.session_state:
    st.session_state.login = False
    st.session_state.token = None

if not st.session_state.login :

    st.subheader("Signup")
    name = st.text_input("Signup Name")
    email = st.text_input("Signup Email")
    password = st.text_input("Signup Password", type="password")

    if st.button("Signup"):
        response = requests.post(
            "http://127.0.0.1:8000/signup",
            json={"name":name,"email": email, "password": password}
        )

        if response.status_code == 200:
            st.success("Signup successful")
            st.session_state.show_login = True
            st.rerun()
        else:
            st.error("Signup failed")

if not st.session_state.login:

    st.subheader("Login")
    email = st.text_input("Login Email")
    password = st.text_input("Login Password", type="password")

    if st.button("Login"):
        response = requests.post(
            "http://127.0.0.1:8000/login",headers={"Authorization": f"Bearer {st.session_state.token}"},
            json={"email": email, "password": password})

        if response.status_code == 200:
            data = response.json()
            st.session_state.login = True
            st.session_state.token = data["token"]
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Invalid credentials")

    if st.button("Logout"):
        st.session_state.login = False
        st.session_state.token = None
        st.session_state.show_login = False
        st.rerun()

if st.session_state.login:

    st.subheader("Create Task")

    title = st.text_input("Title")
    description = st.text_input("Description")
    due_date = st.text_input("Due Date (YYYY-MM-DD)")
    priority = st.selectbox("Priority", ["Low", "Medium", "High"])

    if st.button("Create Task"):
        res = requests.post("http://127.0.0.1:8000/create-task",headers={"Authorization": f"Bearer {st.session_state.token}"},
            json={"title": title,"description": description,"due_date": due_date,"priority": priority } )

        if res.status_code == 200:
            st.success("Task created")

    st.subheader("Update Task")

    task_id = st.number_input("Enter task id")
    title = st.text_input("Title")
    description = st.text_input("Description")
    due_date = st.text_input("Due Date (YYYY-MM-DD)")
    priority = st.selectbox("Priority", ["Low", "Medium", "High"])

    if st.button("Update Task"):
        res = requests.put("http://127.0.0.1:8000/tasks/{task_id}",headers={"Authorization": f"Bearer {st.session_state.token}"},
            json={"title": title,"description": description,"due_date": due_date,"priority": priority } )

        if res.status_code == 200:
            st.success("Task Updated")
    
    st.subheader("Delete Task")

    task_id = st.number_input("Enter task id")

    if st.button("Update Task"):
        res = requests.put("http://127.0.0.1:8000/delete/{task_id}",headers={"Authorization": f"Bearer {st.session_state.token}"},
            json={"title": title,"description": description,"due_date": due_date,"priority": priority } )

        if res.status_code == 200:
            st.success("Task Deleted")
            