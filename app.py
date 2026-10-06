import streamlit as st
import requests

st.set_page_config(page_title="AI Travel Assistant", page_icon="✈️")

st.title("✈️ AI Travel Assistant")
st.write("Ask me anything about your travel plans!")

prompt = st.chat_input("Where do you want to travel?")

if prompt:
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Planning your trip..."):
            response = requests.post(
                "http://127.0.0.1:11434/api/generate",
                json={
                    "model": "llama3.2",
                    "prompt": prompt,
                    "stream": False
                },
                timeout=120
            )

            if response.status_code == 200:
                answer = response.json()["response"]
                st.write(answer)
            else:
                st.error("Ollama connection error.")