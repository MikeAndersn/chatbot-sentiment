import streamlit as st
from chatbot import get_response
from sentiment import analyze_sentiment

st.title("AI Chatbot with Sentiment 💬")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", "")

if user_input:
    sentiment, emoji = analyze_sentiment(user_input)
    response = get_response(user_input, sentiment)

    st.session_state.chat_history.append((user_input, sentiment, emoji, response))

# Display full chat history
for i, (msg, mood, emoji, reply) in enumerate(st.session_state.chat_history):
    st.markdown(f"**You:** {msg}")
    st.markdown(f"**Bot ({mood}) {emoji}:** {reply}")
    st.markdown("---")
