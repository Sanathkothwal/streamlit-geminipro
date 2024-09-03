import google.generativeai as genai
import os
import streamlit as st

Google_api = 'AIzaSyAIWQXFkWw18_4asY32dcVla4q2diy-sDg'
genai.configure(api_key = Google_api)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
def get_gemini_response(input):
    resp = model.generate_content(input)
    return resp

st.set_page_config(page_title="Q$A project")
st.header("Gemini Streamlit end project")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]

input=st.text_input("Input:", key="input")
submit = st.button("Ask the question")

if submit and input:
    response = get_gemini_response(input=input)
    st.session_state["chat_history"].append(("You",input))
    st.subheader("Yoo response is")
    full_resp = ""
    for chunk in response:
        full_resp = full_resp + chunk.text
    st.session_state['chat_history'].append(("Bot", full_resp))
    st.write(full_resp)

st.subheader("Chat History")
for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")