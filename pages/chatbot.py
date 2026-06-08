import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.groq_helper import ask_groq

st.set_page_config(
    page_title="EPM Chatbot · EPM Assistant",
    page_icon="💬",
    layout="wide"
)

st.markdown("""
<style>
    .page-tag {
        display: inline-flex;
        background: #EEEDFE;
        color: #534AB7;
        font-size: 12px;
        font-weight: 500;
        padding: 4px 14px;
        border-radius: 20px;
        margin-bottom: 12px;
    }
    .divider {
        height: 0.5px;
        background: #e0e0e0;
        margin: 20px 0;
    }
    .user-msg {
        background: #E6F1FB;
        border-radius: 12px 12px 2px 12px;
        padding: 12px 16px;
        font-size: 14px;
        color: #0C447C;
        margin-bottom: 8px;
        max-width: 80%;
        margin-left: auto;
    }
    .ai-msg {
        background: #f8f8f8;
        border: 0.5px solid #e0e0e0;
        border-radius: 12px 12px 12px 2px;
        padding: 12px 16px;
        font-size: 14px;
        color: #333;
        margin-bottom: 8px;
        max-width: 85%;
    }
    .quick-btn {
        background: #EEEDFE;
        color: #534AB7;
        border: 0.5px solid #AFA9EC;
        border-radius: 20px;
        padding: 6px 14px;
        font-size: 12px;
        cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)

# ── Header ──
st.markdown('<div class="page-tag">💬 EPM Chatbot</div>',
            unsafe_allow_html=True)
st.markdown("## EPM Support Chatbot")
st.markdown(
    "Ask anything about Oracle EPM, PBCS, FDMEE, or data integration — "
    "get domain-specific answers instantly."
)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── Chat history ──
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ── Quick questions ──
st.markdown(
    '<p style="font-size:12px;color:#888;">Quick questions:</p>',
    unsafe_allow_html=True
)

q1, q2, q3, q4 = st.columns(4)
quick_question = None

with q1:
    if st.button("What is FDMEE?"):
        quick_question = "What is FDMEE and what is it used for in Oracle EPM?"
with q2:
    if st.button("Unmapped member fix"):
        quick_question = (
            "How do I fix unmapped member error in FDMEE data load?"
        )
with q3:
    if st.button("Period mapping setup"):
        quick_question = "How to set up period mapping in Data Management?"
with q4:
    if st.button("Check step failed"):
        quick_question = (
            "Why does the check step fail after a successful data load?"
        )

SYSTEM_PROMPT = """
You are an Oracle EPM Support Specialist with 10+ years of experience 
in PBCS, EPBCS, FDMEE, Essbase, and HFM.

Answer questions about:
- Oracle EPM Cloud (PBCS, EPBCS, FCCS, ARCS)
- FDMEE / Data Management
- Essbase / Smart View
- Data integration, member mappings, data load rules
- EPM Automate, Groovy scripts, calculation scripts
- Troubleshooting and best practices

Rules:
- Be specific and practical
- Use Oracle EPM terminology
- Give step-by-step answers when relevant
- Keep answers concise but complete
- If asked something unrelated to EPM, politely redirect
"""

# ── Process quick question ──
if quick_question:
    st.session_state.chat_history.append({
        "role": "user",
        "content": quick_question
    })
    with st.spinner("Thinking..."):
        response = ask_groq(SYSTEM_PROMPT, quick_question)
    st.session_state.chat_history.append({
        "role": "assistant",
        "content": response
    })

# ── Display chat history ──
if st.session_state.chat_history:
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.markdown(
                f'<div class="user-msg">🧑 {msg["content"]}</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div class="ai-msg">🤖 {msg["content"]}</div>',
                unsafe_allow_html=True
            )

# ── Input ──
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
user_input = st.text_input(
    label="Ask your EPM question",
    placeholder="e.g. How do I fix a period mapping error in FDMEE?",
    key="chat_input"
)

col_send, col_clear = st.columns([4, 1])
with col_send:
    if st.button("Send ↗", type="primary", use_container_width=True):
        if user_input.strip():
            st.session_state.chat_history.append({
                "role": "user",
                "content": user_input
            })
            with st.spinner("Thinking..."):
                response = ask_groq(SYSTEM_PROMPT, user_input)
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": response
            })
            st.rerun()
        else:
            st.warning("Please type a question first.")

with col_clear:
    if st.button("Clear", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown(
    '<p style="font-size:12px;color:#888;text-align:center">'
    'Powered by LLaMA 3.3 70B via Groq API · '
    'Built by Abhishek Singh</p>',
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)
st.page_link("app.py", label="← Back to Home")