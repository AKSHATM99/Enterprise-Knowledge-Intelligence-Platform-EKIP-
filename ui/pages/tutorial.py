import streamlit as st

# 1. Configuration - (MUST be at the very top of the file)
# Note: In newer Streamlit versions, you can call this on subpages too!
st.set_page_config(page_title="EKIP Tutorial", layout="wide")

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
    
    <p class="gradient-text">Tutorial</p>
    <p class="subtitle-text">Master the EKIP workflow and optimize your document intelligence.</p>
    """, unsafe_allow_html=True)