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

if submit_button :
  question_list = []
  answer_list = []
  
  if no_question<=0:
    st.error("Number of question should be greater than zero")
  else:
    if test_type == "objective":
      objective_generator = ObjectiveTest(user_input, no_question)
      question_list, answer_list = objective_generator.generate_test()
    elif test_type == "subjective":
      subjective_generator = SubjectiveTest(user_input, no_question)
      question_list, answer_list = subjective_generator.generate_test()

     # Check for None or empty lists before displaying
    if not question_list or not answer_list:
        st.error("Error: Failed to generate questions or answers.")
    else:
        st.write("### Generated Test")
        for i, (question, answer) in enumerate(zip(question_list, answer_list), start=1):
            st.write(f"**Q{i}:** {question}")
            st.write(f"**A{i}:** {answer}")
    
    
