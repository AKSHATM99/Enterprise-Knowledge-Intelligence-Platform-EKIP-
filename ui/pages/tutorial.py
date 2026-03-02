import streamlit as st

st.set_page_config(page_title="EKIP Tutorial", page_icon="🚀", layout="wide")

# -------------------------
# Custom CSS Styling
# -------------------------
st.markdown("""
<style>

.main {
    background-color: #0f172a;
}

.hero {
    padding: 3rem 2rem;
    border-radius: 20px;
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    color: white;
    text-align: center;
}

.card {
    background-color: #1e293b;
    padding: 1.5rem;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-5px);
}

.section-title {
    font-size: 28px;
    font-weight: 700;
    margin-top: 40px;
    margin-bottom: 20px;
}
.block-container {
            padding-top: 2.5rem !important; /* Reduced from 6rem to 1.5rem */
            padding-bottom: 0rem !important;
            padding-left: 5rem !important;
            padding-right: 5rem !important;
        }
.small-text {
    color: #cbd5e1;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# Hero Section
# -------------------------
st.markdown("""
<div class="hero">
    <h1>🚀 Welcome to EKIP</h1>
    <h3>Intelligent Knowledge Processing</h3>
    <p>AI-powered Document + Database Assistant with Retrieval-Augmented Generation</p>
</div>
""", unsafe_allow_html=True)

st.markdown("")

# -------------------------
# Features Section
# -------------------------
st.markdown('<div class="section-title">✨ What EKIP Can Do</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h4>📄 Document Intelligence</h4>
        <p class="small-text">
        Upload PDFs → Chunk → Embed → Store → Retrieve intelligently.
        Get source-backed answers from your documents.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h4>🗄️ Database Queries</h4>
        <p class="small-text">
        Ask natural language questions.
        EKIP converts them into SQL and fetches precise structured data.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h4>🤖 General AI Assistant</h4>
        <p class="small-text">
        Handles open-ended queries using LLM.
        Fast, concise and intelligent responses.
        </p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------
# How It Works
# -------------------------
st.markdown('<div class="section-title">🧠 How EKIP Works</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
<p class="small-text">

1️⃣ Query is converted into embeddings  
2️⃣ Similarity search performed in Vector Database  
3️⃣ Top relevant chunks retrieved  
4️⃣ Context sent to LLM  
5️⃣ Response generated with confidence score  

</p>
</div>
""", unsafe_allow_html=True)

# -------------------------
# Using EKIP
# -------------------------
st.markdown('<div class="section-title">📘 How To Use EKIP</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h4>📂 Step 1: Upload Documents</h4>
        <p class="small-text">
        Go to Upload Page → Add PDFs → Wait for ingestion confirmation.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h4>💬 Step 2: Ask Questions</h4>
        <p class="small-text">
        Ask document-specific, database, or general AI questions.
        </p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------
# Confidence Section
# -------------------------
st.markdown('<div class="section-title">📊 Confidence Scoring</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
<p class="small-text">

🟢 High Confidence → Similarity > 0.7  
🟡 Medium Confidence → 0.4 – 0.7  
🔴 Low Confidence → Below threshold  

If confidence is low, EKIP may respond with <b>"I don't know"</b>.

</p>
</div>
""", unsafe_allow_html=True)

# -------------------------
# Best Practices
# -------------------------
st.markdown('<div class="section-title">⚙️ Best Practices</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
<p class="small-text">

✔ Ask specific questions  
✔ Use keywords from documents  
✔ Upload text-based PDFs (not scanned images)  
✔ Avoid overly broad queries  

</p>
</div>
""", unsafe_allow_html=True)

st.markdown("")

# Footer
st.markdown("""
<div style="text-align:center; margin-top:40px; color:#94a3b8;">
    EKIP © 2026 | Intelligent Knowledge Processing Platform
</div>
""", unsafe_allow_html=True)