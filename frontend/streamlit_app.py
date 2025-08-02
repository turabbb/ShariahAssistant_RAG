import streamlit as st
import requests

st.set_page_config(
    page_title="Shariah law Assistant",
    page_icon="📖"
)

st.title("📖 Shariah Law Assistant")
st.write("Ask a question about the Quran, Hadith, or Shariah law. This assistant will provide a factual answer based on our document collection.")

API_URL = "http://localhost:8000/ask"

user_query = st.text_input("Enter your question here:")

if user_query:
    with st.spinner("Searching for an answer..."):
        try:
            response = requests.post(API_URL, json={"question": user_query})
            response.raise_for_status()
        
            answer = response.json().get("answer")
            
            st.markdown("### Answer")
            st.write(answer)
        except requests.exceptions.ConnectionError:
            st.error("Connection error. Is the FastAPI server running?")
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")