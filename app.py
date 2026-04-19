import os
import streamlit as st
from anthropic import Anthropic, AuthenticationError, APIError
from pathlib import Path

st.set_page_config(page_title="AI Support Chatbot", page_icon="💬")

# Load knowledge base
kb_path = Path(__file__).parent / "knowledge_base.md"
if not kb_path.exists():
    st.error(
        "knowledge_base.md not found. Please create one in the project root."
    )
    st.stop()

knowledge = kb_path.read_text()

SYSTEM_PROMPT = f"""You are a friendly and helpful customer support assistant for Stride Shoes.
Answer questions using ONLY the information provided in the knowledge base below.
If the answer is not in the knowledge base, say so honestly and suggest the customer
contact support at support@strideshoes.com or call 1-800-555-SHOE.
Be concise, accurate, and warm.

KNOWLEDGE BASE:
{knowledge}"""

# Sidebar
with st.sidebar:
    st.title("💬 AI Support Chatbot")
    st.markdown("A demo customer support chatbot powered by Claude.")
    st.markdown("---")
    st.markdown("**Customize it:** Edit `knowledge_base.md` with your own business info.")
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Initialize conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize Anthropic client
if not os.environ.get("ANTHROPIC_API_KEY"):
    st.error(
        "ANTHROPIC_API_KEY environment variable not set. "
        "Copy .env.example to .env and add your key, then restart the app."
    )
    st.stop()

try:
    client = Anthropic()
except Exception:
    st.error(
        "Could not initialize the Anthropic client. "
        "Make sure ANTHROPIC_API_KEY is set correctly."
    )
    st.stop()

# Display conversation history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Handle new user input
if prompt := st.chat_input("How can I help you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    try:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=st.session_state.messages,
        )
        reply = response.content[0].text
    except AuthenticationError:
        reply = (
            "Authentication failed. Please check that your ANTHROPIC_API_KEY is valid."
        )
    except APIError as e:
        reply = f"The API returned an error. Please try again. (Error: {e})"
    except Exception as e:
        reply = f"Something went wrong. Please try again. (Error: {e})"

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)
