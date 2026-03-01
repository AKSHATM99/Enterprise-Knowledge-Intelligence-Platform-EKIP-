import streamlit as st
import httpx
import os

# --- Page Config ---
st.set_page_config(page_title="EKIP Chat", page_icon="📄", layout="wide")

st.markdown("""
    <style>
        /* --- REDUCE TOP MARGIN --- */
        /* Targets the main content area */
        .stAppViewBlockContainer {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
        }
        
        /* Removes the top gap of the first element */
        .stMainBlockContainer {
            margin-top: -50px !important;
        }

        /* --- YOUR STYLING --- */
        .gradient-text {
            font-size: 40px !important;
            font-weight: 700 !important;
            background: linear-gradient(90deg, #DC244C, #7B2FF7);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
            line-height: 1.2;
        }
        .subtitle-text {
            color: #94A3B8;
            font-size: 1.2rem; /* Adjusted from 50.1rem */
            margin-bottom: 2rem;
        }
    </style>
    
    <p class="gradient-text">Interact with your Docs</p>
    <p class="subtitle-text">Chat with your knowledge base using high-performance vector search.</p>
    """, unsafe_allow_html=True)

# Define your FastAPI endpoint (override in Docker with env var)
FASTAPI_ENDPOINT = os.getenv("FASTAPI_ENDPOINT", "http://localhost:8000/query/")

# Initialize chat history if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
if prompt := st.chat_input("Ask a question about your docs..."):
    # 1. Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. Get Response from FastAPI
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Using the synchronous Client for simplicity in Streamlit
                with httpx.Client() as client:
                    response = client.post(
                        FASTAPI_ENDPOINT, 
                        json={"question": prompt},
                        timeout=30.0
                    )
                    response.raise_for_status() # Check for HTTP errors
                    
                    data = response.json()
                    answer = data.get("answer")
                    sources = data.get("sources")
                    
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer, "sources": sources})
            
            except httpx.ConnectError:
                st.error("Failed to connect to the FastAPI server. Is it running?")
            except Exception as e:
                st.error(f"An error occurred: {e}")