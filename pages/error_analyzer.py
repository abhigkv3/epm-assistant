import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.groq_helper import ask_groq

st.set_page_config(
    page_title="Error Analyzer · EPM Assistant",
    page_icon="🔍",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .page-tag {
        display: inline-flex;
        align-items: center;
        background: #E6F1FB;
        color: #185FA5;
        font-size: 12px;
        font-weight: 500;
        padding: 4px 14px;
        border-radius: 20px;
        margin-bottom: 12px;
    }
    .info-card {
        background: #E6F1FB;
        border: 0.5px solid #B5D4F4;
        border-radius: 12px;
        padding: 16px 20px;
        margin-bottom: 20px;
    }
    .result-card {
        background: #EAF3DE;
        border: 0.5px solid #C0DD97;
        border-radius: 12px;
        padding: 20px 24px;
        margin-top: 20px;
    }
    .error-type-badge {
        background: #FCEBEB;
        color: #A32D2D;
        font-size: 12px;
        font-weight: 500;
        padding: 4px 12px;
        border-radius: 10px;
        display: inline-block;
        margin-bottom: 12px;
    }
    .step-box {
        background: white;
        border: 0.5px solid #e0e0e0;
        border-radius: 8px;
        padding: 12px 16px;
        margin-top: 10px;
        font-size: 14px;
    }
    .divider {
        height: 0.5px;
        background: #e0e0e0;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# ── Header ──
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('<div class="page-tag">🔍 Error Analyzer</div>',
                unsafe_allow_html=True)
    st.markdown("## Data Load Error Analyzer")
    st.markdown(
        "Paste your Process Details error — AI will identify the root cause "
        "and provide step-by-step resolution guidance."
    )
with col2:
    st.markdown("""
    <div style="background:#f8f8f8;border-radius:10px;
                padding:12px 16px;margin-top:8px;font-size:12px">
        <div style="font-weight:600;margin-bottom:8px;color:#333">
            Supported errors
        </div>
        <div style="color:#666;line-height:2">
            ✓ Unmapped member<br>
            ✓ File parse errors<br>
            ✓ Period mapping issues<br>
            ✓ Check step variance<br>
            ✓ Export failures
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── Info box ──
st.markdown("""
<div class="info-card">
    <div style="font-weight:500;font-size:14px;color:#185FA5;margin-bottom:4px">
        How to use
    </div>
    <div style="font-size:13px;color:#0C447C;line-height:1.7">
        Go to <strong>FDMEE → Workflow → Process Details</strong> → 
        copy the error message from the Import, Validate, or Export tab 
        → paste it below → click Analyze.
    </div>
</div>
""", unsafe_allow_html=True)

# ── Input ──
error_input = st.text_area(
    label="Paste your error message here",
    height=180,
    placeholder="Example: No mapping found for member '450099' "
                "in dimension 'Account' for location 'IN_Entity'..."
)

# ── Example errors ──
st.markdown(
    '<p style="font-size:12px;color:#888;margin-top:6px">'
    'Try an example:</p>',
    unsafe_allow_html=True
)

ex1, ex2, ex3 = st.columns(3)
with ex1:
    if st.button("📌 Unmapped member error"):
        error_input = (
            "No mapping found for member '450099' "
            "in dimension 'Account'"
        )
with ex2:
    if st.button("📌 File parse error"):
        error_input = (
            "File could not be parsed. "
            "Invalid delimiter found in source file."
        )
with ex3:
    if st.button("📌 Check step variance"):
        error_input = (
            "Check failed. Source amount: 5000000, "
            "Loaded amount: 4500000. Variance: 500000"
        )

st.markdown("<br>", unsafe_allow_html=True)

# ── Analyze button ──
SYSTEM_PROMPT = """
You are an Oracle EPM/PBCS/FDMEE data integration expert with 10+ years 
of experience in production support.

When analyzing an error:
1. Start with: "Error Type:" — identify the exact error category
2. "Root Cause:" — explain why this happens in simple terms
3. "Where to Check:" — exact navigation path in FDMEE/Data Management
4. "Step-by-step Fix:" — numbered steps to resolve
5. "Prevention:" — one line on how to avoid this in future

Be specific, practical, and concise. Use Oracle EPM terminology.
"""

if st.button("🔍  Analyze Error", type="primary", use_container_width=True):
    if not error_input or error_input.strip() == "":
        st.warning("Please paste an error message before analyzing.")
    else:
        with st.spinner("Analyzing error — please wait..."):
            response = ask_groq(SYSTEM_PROMPT, error_input)

        st.markdown("""
        <div class="result-card">
            <div style="font-weight:600;font-size:16px;
                        color:#27500A;margin-bottom:4px">
                Analysis Complete
            </div>
            <div style="font-size:12px;color:#3B6D11;margin-bottom:16px">
                Root cause identified · Fix steps provided
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Resolution Guide")
        st.markdown(response)

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        st.markdown(
            '<p style="font-size:12px;color:#888;text-align:center">'
            'Analysis powered by LLaMA 3.3 70B via Groq API · '
            'Built by Abhishek Singh</p>',
            unsafe_allow_html=True
        )

# ── Back button ──
st.markdown("<br>", unsafe_allow_html=True)
st.page_link("app.py", label="← Back to Home")