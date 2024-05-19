from dotenv import load_dotenv
load_dotenv()  # import all env variable

import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
#fn to load Gemini model get responses
model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

##streamlit app

st.set_page_config(page_title="Q&A")

st.header("Gemini LLM Application")
    
input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(input)
    st.write(response)


