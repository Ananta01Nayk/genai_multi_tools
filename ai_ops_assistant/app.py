import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from backend import chatbot

st.set_page_config(page_title="LangGraph Chatbot", layout="centered")

st.title("LangGraph Tool-Calling Chatbot")

# -----------------------------
# Simple in-memory chat history
# -----------------------------
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Render previous messages
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.session_state["messages"].append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    # Assistant response (streaming)
    with st.chat_message("assistant"):
        status_box = {"ref": None}

        def stream_response():
            for message, _ in chatbot.stream(
                {"messages": [HumanMessage(content=user_input)]},
                stream_mode="messages",
            ):
                # Show tool usage
                if isinstance(message, ToolMessage):
                    tool_name = getattr(message, "name", "tool")
                    if status_box["ref"] is None:
                        status_box["ref"] = st.status(
                            f"🔧 Using `{tool_name}`", expanded=True
                        )
                    else:
                        status_box["ref"].update(
                            label=f"🔧 Using `{tool_name}`",
                            state="running",
                            expanded=True,
                        )

                # Stream assistant text
                if isinstance(message, AIMessage):
                    yield message.content

        assistant_reply = st.write_stream(stream_response)

        if status_box["ref"] is not None:
            status_box["ref"].update(
                label="✅ Tool finished",
                state="complete",
                expanded=False,
            )

    # Save assistant reply
    st.session_state["messages"].append(
        {"role": "assistant", "content": assistant_reply}
    )
