import streamlit as st

st.set_page_config(page_title="Welcome", layout="wide")

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
    
    <p class="gradient-text">Welcome to Ekip!</p>
    <p class="subtitle-text">Enterprise Knowledge Intelligence Platform (EKIP)</p>
    """, unsafe_allow_html=True)

# Hero Section
# st.markdown("### Enterprise Knowledge Intelligence Platform (EKIP)")
# st.write("---")

# Layout with Columns (Cards)
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total Points", value="1.2M", delta="12% 📈")
    st.caption("Vectors currently indexed")

with col2:
    st.metric(label="Collections", value="24", delta="0")
    st.caption("Active data namespaces")

with col3:
    st.metric(label="Latency", value="4ms", delta="-1ms ⚡")
    st.caption("Search p95 response time")

# st.write("## Quick Actions")
# c1, c2 = st.columns(2)

# with c1:
#     with st.container(border=True):
#         st.write("#### 🔍 Search Collections")
#         st.write("Run similarity searches across your high-dimensional data.")
#         # Logic to switch page
#         if st.button("Open Dashboard", use_container_width=True):
#             st.switch_page("pages/dashboard.py")

# with c2:
#     with st.container(border=True):
#         st.write("#### 🛠️ API Console")
#         st.write("Direct HTTP/gRPC interface for database management.")
#         # Logic to switch page
#         if st.button("Launch Console", use_container_width=True):
#             st.switch_page("pages/console.py")