
import streamlit as st
import openai
from openai import OpenAI

st.set_page_config(page_title="AA Assistant Chatbot", layout="wide")

# --- Sidebar ---
st.sidebar.title("AA Assistant Chatbot")
st.sidebar.info("Hi! I’m AA Assistant, here to answer questions about Adewale Adenuga. Type your question and I’ll respond with info from his experience and background.")
api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")

# --- Greeting ---
st.title("👋 Welcome to AA Assistant")
st.markdown("HI, welcome home! I am Adewale, where project timelines meet customer insights and Python speaks business fluently. Need a dashboard, a model or a CRM health check? Hit me up or leave your contact and I will reach out shortly.")

# --- Load Context ---
context = """
You are AA Assistant, a helpful chatbot representing Adewale Adenuga. Your job is to professionally and clearly answer questions about Adewale's background, skills, and experience based on the context provided.

Greeting message:
"HI, welcome home! I am Adewale, where project timelines meet customer insights and Python speaks business fluently. Need a dashboard, a model or a CRM health check? Hit me up or leave your contact and I will reach out shortly."

If the user asks for contact or a follow-up, respond with:
"Feel free to email Adewale at adewaleadenuga483@gmail.com or call +49 152 158 06607."

Use the following professional context to answer user questions:
Adewale Adenuga is a certified Project Manager (PMP®) and skilled Data Analyst/Data Scientist. He is experienced in transforming business data into strategic actions using tools like Python, Power BI, SQL, Excel, and Tableau. Adewale has led CRM projects, automated data pipelines, built predictive models, and delivered interactive dashboards for business intelligence. His background spans industries including telecom, tech, and education. He’s fluent in project delivery, customer analytics, and process optimization.
"""

# --- Input ---
client = OpenAI(api_key=api_key)
if api_key:
    openai.api_key = api_key
    user_input = st.text_input("Ask me anything about Adewale...", key="user_input")

    if user_input:
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": context},
                        {"role": "user", "content": user_input}
                    ],
                    max_tokens=500,
                    temperature=0.7
                )
                answer = response.choices[0].message.content
                st.success(answer)
            
            except Exception as e:
                st.error(f"Something went wrong: {e}")
else:
    st.warning("Please enter your OpenAI API key in the sidebar to start chatting.")
