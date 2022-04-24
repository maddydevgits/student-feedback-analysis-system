import app1_student_feedback
import app2_subject1_feedback
import app3_subject2_feedback
import app4_subject3_feedback
import app5_subject4_feedback



import streamlit as st
PAGES = {
    "Student Feedback": app1_student_feedback,
    "Subject1 Feedback": app2_subject1_feedback,
    "Subject2 Feedback": app3_subject2_feedback,
    "Subject3 Feedback": app4_subject3_feedback,
    "Subject4 Feedback": app5_subject4_feedback
}
st.sidebar.title('Dashboard')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()