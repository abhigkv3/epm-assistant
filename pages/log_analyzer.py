import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.groq_helper import ask_groq

st.set_page_config(
    page_title="Log Analyzer · EPM Assistant",
    page_icon="📋",
    layout="wide"
)

st.markdown("""
<style>
    .page-tag {
        display: inline-flex;
        background: #E1F5EE;
        color: #0F6E56;
        font-size: 12px;
        font-weight: 500;
        padding: 4px 14px;
        border-radius: 20px;
        margin-bottom: 12px;
    }
    .info-card {
        background: #E1F5EE;
        border: 0.5px solid #9FE1CB;
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
    .divider {
        height: 0.5px;
        background: #e0e0e0;
        margin: 20px 0;
    }
    .upload-box {
        background: #f8f8f8;
        border: 1.5px dashed #ccc;
        border-radius: 12px;
        padding: 24px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# ── Header ──
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('<div class="page-tag">📋 Log Analyzer</div>',
                unsafe_allow_html=True)
    st.markdown("## FDMEE Log Analyzer")
    st.markdown(
        "Upload your FDMEE log file — AI will scan for error patterns, "
        "recurring issues, and generate a prioritized summary report."
    )
with col2:
    st.markdown("""
    <div style="background:#f8f8f8;border-radius:10px;
                padding:12px 16px;margin-top:8px;font-size:12px">
        <div style="font-weight:600;margin-bottom:8px;color:#333">
            What AI detects
        </div>
        <div style="color:#666;line-height:2">
            ✓ Error frequency<br>
            ✓ Recurring patterns<br>
            ✓ Critical vs minor issues<br>
            ✓ Affected dimensions<br>
            ✓ Recommended actions
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── Info box ──
st.markdown("""
<div class="info-card">
    <div style="font-weight:500;font-size:14px;
                color:#0F6E56;margin-bottom:4px">
        How to use
    </div>
    <div style="font-size:13px;color:#085041;line-height:1.7">
        Go to <strong>FDMEE → Workflow → Process Details</strong> → 
        select any completed process → click <strong>View Log</strong> → 
        save the log file → upload it below.
    </div>
</div>
""", unsafe_allow_html=True)

# ── File upload ──
uploaded_file = st.file_uploader(
    label="Upload FDMEE log file",
    type=["txt", "log"],
    help="Supported formats: .txt, .log"
)

SYSTEM_PROMPT = """
You are an Oracle EPM/FDMEE log analysis expert.

When analyzing a log file:
1. "Summary:" — 2-3 lines overview of what happened
2. "Critical Issues:" — errors that caused load failure (if any)
3. "Warnings:" — non-critical issues that need attention
4. "Recurring Patterns:" — errors appearing multiple times
5. "Affected Dimensions/Members:" — which dimensions had issues
6. "Recommended Actions:" — prioritized fix list (P1, P2, P3)
7. "Overall Health:" — Good / Needs Attention / Critical

Be specific, use Oracle EPM terminology, keep it concise.
"""

if uploaded_file is not None:
    log_content = uploaded_file.read().decode("utf-8", errors="ignore")

    # File info
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown(f"""
        <div style="background:#f8f8f8;border-radius:8px;
                    padding:12px;text-align:center;margin-top:12px">
            <div style="font-size:18px;font-weight:600">
                {uploaded_file.name}
            </div>
            <div style="font-size:12px;color:#888">File name</div>
        </div>""", unsafe_allow_html=True)
    with col_b:
        size_kb = round(len(log_content.encode()) / 1024, 1)
        st.markdown(f"""
        <div style="background:#f8f8f8;border-radius:8px;
                    padding:12px;text-align:center;margin-top:12px">
            <div style="font-size:18px;font-weight:600">{size_kb} KB</div>
            <div style="font-size:12px;color:#888">File size</div>
        </div>""", unsafe_allow_html=True)
    with col_c:
        line_count = len(log_content.splitlines())
        st.markdown(f"""
        <div style="background:#f8f8f8;border-radius:8px;
                    padding:12px;text-align:center;margin-top:12px">
            <div style="font-size:18px;font-weight:600">{line_count}</div>
            <div style="font-size:12px;color:#888">Total lines</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Preview
    with st.expander("Preview log content (first 50 lines)"):
        preview = "\n".join(log_content.splitlines()[:50])
        st.code(preview, language="text")

    # Analyze button
    if st.button("📋  Analyze Log File", type="primary",
                 use_container_width=True):
        # Limit to first 3000 chars to avoid token limit
        log_trimmed = log_content[:3000]

        with st.spinner("Scanning log file — please wait..."):
            response = ask_groq(SYSTEM_PROMPT, log_trimmed)

        st.markdown("""
        <div class="result-card">
            <div style="font-weight:600;font-size:16px;
                        color:#27500A;margin-bottom:4px">
                Log Analysis Complete
            </div>
            <div style="font-size:12px;color:#3B6D11;margin-bottom:16px">
                Patterns detected · Issues prioritized
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Analysis Report")
        st.markdown(response)

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        st.markdown(
            '<p style="font-size:12px;color:#888;text-align:center">'
            'Analysis powered by LLaMA 3.3 70B via Groq API · '
            'Built by Abhishek Singh</p>',
            unsafe_allow_html=True
        )

else:
    st.markdown("""
    <div class="upload-box">
        <div style="font-size:32px;margin-bottom:8px">📂</div>
        <div style="font-size:14px;font-weight:500;color:#555">
            Upload a .log or .txt file to get started
        </div>
        <div style="font-size:12px;color:#888;margin-top:4px">
            FDMEE process log recommended
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.page_link("app.py", label="← Back to Home")