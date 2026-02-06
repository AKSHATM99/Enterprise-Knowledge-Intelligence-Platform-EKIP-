import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="EKIP Engine", page_icon="🚀", layout="wide")

# 2. Custom CSS for Branding
st.markdown("""
    <style>
        /* Main Hero Title */
        .hero-text {
            font-size: 60px !important;
            font-weight: 800 !important;
            text-align: center;
            background: linear-gradient(90deg, #DC244C, #7B2FF7);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0px;
        }
        
        .hero-subtitle {
            font-size: 1.5rem;
            color: #94A3B8;
            text-align: center;
            margin-bottom: 50px;
        }

        /* Feature Card Styling */
        .feature-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 30px;
            text-align: center;
            height: 100%;
            transition: transform 0.3s ease;
        }
        
        .feature-card:hover {
            transform: translateY(-10px);
            border-color: #DC244C;
        }

        .feature-icon {
            font-size: 40px;
            margin-bottom: 15px;
        }

        .feature-title {
            color: white;
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 10px;
        }

        .feature-desc {
            color: #94A3B8;
            font-size: 0.95rem;
        }
            

        /* 1. Keep the header but make its background transparent (optional) */
        header {
            background-color: transparent !important;
        }

        /* 2. Target the main content container specifically */
        .block-container {
            padding-top: 1.5rem !important; /* Reduced from 6rem to 1.5rem */
            padding-bottom: 0rem !important;
            padding-left: 5rem !important;
            padding-right: 5rem !important;
        }

        /* 3. Adjust the vertical block spacing */
        .stVerticalBlock {
            gap: 1rem !important;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Hero Section
st.markdown('<h1 class="hero-text">EKIP Intelligence Engine</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Enterprise Knowledge Intelligence Platform (EKIP)</p>', unsafe_allow_html=True)

# 4. Features Grid
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🔌</div>
            <div class="feature-title">Multi-Source Ingestion</div>
            <div class="feature-desc">Connect S3, ServiceNow, GitHub, and local files in seconds.</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🧠</div>
            <div class="feature-title">RAG-Powered Search</div>
            <div class="feature-desc">Utilize Retrieval-Augmented Generation for context-aware AI answers.</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🛡️</div>
            <div class="feature-title">Enterprise Security</div>
            <div class="feature-desc">End-to-end encryption for your sensitive corporate documentation.</div>
        </div>
    """, unsafe_allow_html=True)

st.write("---")

# 5. Call to Action (The "Gateway")
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    st.info("💡 **Pro-Tip:** Start by adding your first data source to train the engine.")
    if st.button("🚀 GET STARTED: ADD NEW SOURCE", use_container_width=True, type="primary"):
        # This assumes you have a page file named 'pages/add_new_source.py'
        st.switch_page("pages/add_new_source.py")
