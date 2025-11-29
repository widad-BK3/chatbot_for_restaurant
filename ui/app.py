# import streamlit as st
# import requests

# st.title("Local AI Agent with RAG")

# question = st.text_input("Ask a question:")
# if st.button("Ask"):
#     response = requests.post("http://127.0.0.1:5000/ask", json={"question": question})
#     if response.status_code == 200:
#         st.text_area("Answer:", response.json().get("answer", ""), height=200)
#     else:
#         st.error("Error connecting to backend")

# _____________________________________________________________
import streamlit as st
import sys
import os

# Make sure Python can find main.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import ask_question

st.title("Local AI Agent with RAG")

# Initialize session state for history
if "history" not in st.session_state:
    st.session_state.history = []

# Input box for user question
question = st.text_input("Ask a question:")

if st.button("Ask"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        # Show spinner while AI generates answer
        with st.spinner("AI is thinking..."):
            answer = ask_question(question)
        
        # Store question and answer in session state
        st.session_state.history.append({"question": question, "answer": answer})

# Display all previous Q&A
if st.session_state.history:
    st.markdown("### Conversation History")
    for i, qa in enumerate(st.session_state.history, 1):
        st.markdown(f"**Q{i}:** {qa['question']}")
        st.markdown(f"**A{i}:** {qa['answer']}")
        st.markdown("---")
