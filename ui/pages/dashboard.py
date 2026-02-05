import streamlit as st

# 1. Configuration - (MUST be at the very top of the file)
# Note: In newer Streamlit versions, you can call this on subpages too!
st.set_page_config(page_title="EKIP Dashboard", layout="wide")

# 2. CSS to eliminate top margin (Your updated version)
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
    
    <p class="gradient-text">Analytics Dashboard</p>
    <p class="subtitle-text">Real-time metrics for your EKIP document engine.</p>
    """, unsafe_allow_html=True)

# # 3. Page Header
# st.title("📊 Analytics Dashboard")
# st.write("Real-time metrics for your EKIP document engine.")

# 4. Top Row Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("QPS", "142", "1.2%")
col2.metric("Success Rate", "99.8%", "0.1%")
col3.metric("Avg Latency", "24ms", "-2ms")
col4.metric("Active Users", "1.2k", "42")

st.divider()

# 5. Main Content Area
left_col, right_col = st.columns([2, 1])

with left_col:
    with st.container(border=True):
        st.subheader("Collection Growth")
        # Placeholder for a chart
        st.line_chart({"Vectors": [10, 25, 45, 80, 120, 180, 250]})

with right_col:
    with st.container(border=True):
        st.subheader("Recent Activity")
        st.write("✅ Indexing: 'legal_docs_v2'")
        st.write("⚠️ Warning: High memory usage in Node 3")
        st.write("✅ Search: Query 'compliance' (0.04s)")