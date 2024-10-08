import streamlit as st
from objective import ObjectiveTest
from subjective import SubjectiveTest

st.title('🎈 QA Generator')
st.write('**Want to Generate Some Question ???**')
st.write('**Enter Some Paragraph !!!**')

with st.form("my_form"):
  user_input = st.text_area("Enter your text here", height=150)
  test_type = st.selectbox('Question Type',('Subjective','Objective'))
  no_question = st.slider('No of Question',1,5,10)
  
  submit_button = st.form_submit_button('Submit my picks')

if submit_button:
  if no_question<=0:
    st.error("Number of question should be greater than zero")
  else:
    if test_type == "objective":
      objective_generator = ObjectiveTest(user_input, no_question)
      question_list, answer_list = objective_generator.generate_test()
    elif test_type == "subjective":
      subjective_generator = SubjectiveTest(user_input, no_question)
      question_list, answer_list = subjective_generator.generate_test()

    # Debugging: Print the lists to verify
    st.write("Debug Info:")
    st.write(f"Questions: {question_list}")
    st.write(f"Answers: {answer_list}")
    
    
