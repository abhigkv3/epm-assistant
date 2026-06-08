import streamlit as st

st.set_page_config(
    page_title="EPM Intelligent Support Assistant",
    page_icon="🏢",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    /* Hero section */
    .hero-tag {
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
    /* Author card */
    .author-card {
        background: white;
        border: 0.5px solid #e0e0e0;
        border-radius: 12px;
        padding: 14px 18px;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .avatar {
        width: 42px;
        height: 42px;
        border-radius: 50%;
        background: #E6F1FB;
        color: #185FA5;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 600;
        font-size: 14px;
    }
    /* Feature cards */
    .feature-card {
        background: white;
        border: 0.5px solid #e0e0e0;
        border-radius: 12px;
        padding: 20px;
        height: 100%;
        transition: border-color 0.2s;
    }
    .feature-card:hover {
        border-color: #378ADD;
    }
    .featured-card {
        background: white;
        border: 2px solid #378ADD;
        border-radius: 12px;
        padding: 20px;
        height: 100%;
    }
    .card-icon-blue {
        background: #E6F1FB;
        color: #185FA5;
        width: 38px;
        height: 38px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
        margin-bottom: 12px;
    }
    .tag-blue {
        background: #E6F1FB;
        color: #185FA5;
        font-size: 11px;
        padding: 3px 10px;
        border-radius: 10px;
        font-weight: 500;
    }
    .tag-teal {
        background: #E1F5EE;
        color: #0F6E56;
        font-size: 11px;
        padding: 3px 10px;
        border-radius: 10px;
        font-weight: 500;
    }
    .tag-purple {
        background: #EEEDFE;
        color: #534AB7;
        font-size: 11px;
        padding: 3px 10px;
        border-radius: 10px;
        font-weight: 500;
    }
    .badge-new {
        background: #E6F1FB;
        color: #185FA5;
        font-size: 11px;
        padding: 2px 10px;
        border-radius: 10px;
        font-weight: 500;
    }
    .tech-pill {
        background: #f5f5f5;
        color: #666;
        font-size: 11px;
        padding: 3px 10px;
        border-radius: 10px;
        border: 0.5px solid #e0e0e0;
        margin-right: 4px;
    }
    .stat-card {
        background: #f8f8f8;
        border-radius: 8px;
        padding: 14px;
        text-align: center;
    }
    .divider {
        height: 0.5px;
        background: #e0e0e0;
        margin: 24px 0;
    }
</style>
""", unsafe_allow_html=True)

# ── Hero Section ──
col_left, col_right = st.columns([2, 1])

with col_left:
    st.markdown('<div class="hero-tag">⚡ AI-powered</div>', 
                unsafe_allow_html=True)
    st.markdown("## EPM Intelligent Support Assistant")
    st.markdown(
        "Automate error diagnosis, log analysis, and troubleshooting "
        "for Oracle EPM/PBCS data integration workflows."
    )

with col_right:
    st.markdown("""
    <div class="author-card">
        <div class="avatar">AS</div>
        <div>
            <div style="font-weight:600;font-size:14px">Abhishek Singh</div>
            <div style="font-size:12px;color:#888">EPM Specialist</div>
            <div style="font-size:12px;color:#888">Physics Wallah Pvt Ltd</div>
            <div style="margin-top:6px;font-size:12px">
                <a href="https://www.linkedin.com/in/abhishek-singh-44699a392/" 
                   style="color:#185FA5;text-decoration:none;margin-right:12px">
                   LinkedIn
                </a>
                <a href="mailto:abhigkv.epm@gmail.com" 
                   style="color:#185FA5;text-decoration:none">
                   Email
                </a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Stats ──
s1, s2, s3 = st.columns(3)
with s1:
    st.markdown("""
    <div class="stat-card">
        <div style="font-size:22px;font-weight:600">3</div>
        <div style="font-size:12px;color:#888;margin-top:2px">AI-powered modules</div>
    </div>""", unsafe_allow_html=True)
with s2:
    st.markdown("""
    <div class="stat-card">
        <div style="font-size:18px;font-weight:600">LLaMA 3.3</div>
        <div style="font-size:12px;color:#888;margin-top:2px">Model (70B)</div>
    </div>""", unsafe_allow_html=True)
with s3:
    st.markdown("""
    <div class="stat-card">
        <div style="font-size:16px;font-weight:600">PBCS · FDMEE</div>
        <div style="font-size:12px;color:#888;margin-top:2px">Domain focus</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Feature Cards ──
st.markdown(
    '<p style="font-size:11px;font-weight:500;color:#888;'
    'letter-spacing:0.08em;text-transform:uppercase">'
    'CHOOSE A MODULE</p>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="featured-card">
        <div style="font-size:24px;margin-bottom:10px">🔍</div>
        <div style="font-weight:600;font-size:15px;margin-bottom:6px">
            Error analyzer
        </div>
        <div style="font-size:13px;color:#666;line-height:1.6;margin-bottom:12px">
            Paste any Process Details error — get instant root cause 
            analysis and step-by-step fix guidance.
        </div>
        <span class="tag-blue">Data load errors</span>
        <div style="margin-top:12px;padding-top:12px;
                    border-top:0.5px solid #eee;
                    display:flex;justify-content:space-between;
                    align-items:center">
            <span class="badge-new">Most used</span>
            <span style="font-size:13px;color:#185FA5">Open →</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/error_analyzer.py", label="Open Error Analyzer")

with c2:
    st.markdown("""
    <div class="feature-card">
        <div style="font-size:24px;margin-bottom:10px">📋</div>
        <div style="font-weight:600;font-size:15px;margin-bottom:6px">
            Log analyzer
        </div>
        <div style="font-size:13px;color:#666;line-height:1.6;margin-bottom:12px">
            Upload FDMEE log files — AI scans for patterns, recurring 
            issues, and generates a priority summary report.
        </div>
        <span class="tag-teal">FDMEE logs</span>
        <div style="margin-top:12px;padding-top:12px;
                    border-top:0.5px solid #eee;
                    display:flex;justify-content:space-between;
                    align-items:center">
            <span style="font-size:12px;color:#888">Upload .log / .txt</span>
            <span style="font-size:13px;color:#185FA5">Open →</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/log_analyzer.py", label="Open Log Analyzer")

with c3:
    st.markdown("""
    <div class="feature-card">
        <div style="font-size:24px;margin-bottom:10px">💬</div>
        <div style="font-weight:600;font-size:15px;margin-bottom:6px">
            EPM chatbot
        </div>
        <div style="font-size:13px;color:#666;line-height:1.6;margin-bottom:12px">
            Ask anything about Oracle EPM — troubleshooting, best 
            practices, configuration — domain-specific answers only.
        </div>
        <span class="tag-purple">Q&amp;A</span>
        <div style="margin-top:12px;padding-top:12px;
                    border-top:0.5px solid #eee;
                    display:flex;justify-content:space-between;
                    align-items:center">
            <span style="font-size:12px;color:#888">Ask anything</span>
            <span style="font-size:13px;color:#185FA5">Open →</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/chatbot.py", label="Open EPM Chatbot")

# ── Footer ──
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown("""
<div style="display:flex;justify-content:space-between;align-items:center">
    <span style="font-size:12px;color:#888">
        Built by Abhishek Singh · Physics Wallah Pvt Ltd
    </span>
    <span>
        <span class="tech-pill">Python</span>
        <span class="tech-pill">Streamlit</span>
        <span class="tech-pill">Groq API</span>
        <span class="tech-pill">LLaMA 3.3</span>
    </span>
</div>
""", unsafe_allow_html=True)