import streamlit as st

st.title('🎈 QA Generator')

st.info('**What to Generate Some Question ???**')

user_input = st.text_area("Enter your text here", height=150)

# Display the entered text
if user_input:
    st.write("You entered:")
    st.write(user_input)
