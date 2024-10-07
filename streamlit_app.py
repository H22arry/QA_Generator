import streamlit as st

st.title('🎈 QA Generator')

st.info('**What to Generate Some Question ???**')

st.info('**Enter Some Paragraph ???**')
user_input = st.text_area("Enter your text here", height=150)
test_type = st.selectbox('Question Type':'Subjective','Objective')
