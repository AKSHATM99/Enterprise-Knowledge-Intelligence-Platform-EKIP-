import streamlit as st

# Set the page config (titles/icons)
st.set_page_config(page_title="EKIP", page_icon="📄", layout="wide")

# --- THE UPDATED CSS ---
st.markdown("""
    <style>
              section[data-testid="stSidebar"] {
        height: 100vh !important;
        overflow: hidden !important;
    }

    section[data-testid="stSidebar"] > div {
        height: 100vh !important;
        overflow: hidden !important;
    }

    section[data-testid="stSidebar"] .stVerticalBlock {
        overflow: hidden !important;
    }
        /* 1. LOCK THE ENTIRE SIDEBAR FROM SCROLLING */
        [data-testid="stSidebarUserContent"] {
            height: 100vh !important;
            overflow: hidden !important;
            display: flex;
            flex-direction: column;
        }

        /* 2. ENSURE NAVIGATION LIST DOESN'T OVERFLOW */
        [data-testid="stSidebarNav"] {
            overflow: hidden !important;
            flex-grow: 1;
        }

        /* 3. Global Sidebar Background */
        [data-testid="stSidebar"] {
            background-color: #0D1117 !important;
            border-right: 2px solid #1E293B !important;
        }

        /* 4. Header Border & Background */
        header[data-testid="stHeader"] {
            visibility: visible !important;
            height: 3.5rem !important;
            background-color: #0D1117 !important;
            border-bottom: 1px solid #1E293B !important; 
            box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
        }
        
        /* 5. Style the Navigation Item Text */
        [data-testid="stSidebarNavItems"] span {
            font-size: 16px !important;
            font-weight: 500 !important;
            color: #8B949E !important; 
            font-family: 'Inter', -apple-system, sans-serif;
            letter-spacing: -0.2px;
            transition: all 0.2s ease;
        }

        /* 6. Navigation Item Container */
        [data-testid="stSidebarNavItems"] li {
            margin-bottom: 4px !important;
            padding-left: 12px !important;
            padding-right: 12px !important;
            border-radius: 8px !important;
        }

        /* 7. The Active Page Styling */
        [data-testid="stSidebarNavItems"] div[aria-selected="true"] {
            background-color: #1F2937 !important;
            border-radius: 8px !important;
        }

        [data-testid="stSidebarNavItems"] div[aria-selected="true"] span {
            color: #FFFFFF !important;
            font-weight: 700 !important;
        }

        /* 8. Hover Effect */
        [data-testid="stSidebarNavItems"] li:hover {
            background-color: rgba(255, 255, 255, 0.05) !important;
        }

        [data-testid="stSidebarNavItems"] li:hover span {
            color: #F0F6FC !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- CUSTOM SIDEBAR CONTENT ---
# We wrap these in a container to ensure they stay fixed
with st.sidebar:
    st.image("assets/logo.png")
    # Spacer to push the version text to the bottom if desired, 
    # or keep it here if you want it under the logo.
    st.markdown("""
        <div style="text-align: center; color: #475569; font-size: 0.8rem; margin-top: 10px; margin-bottom: 20px;">
            EKIP Engine v1.0.4 • Built for High-Performance Teams
        </div>
    """, unsafe_allow_html=True)

# Define the pages
pages = [
    st.Page("pages/welcome.py", title="Welcome", default=True),
    st.Page("pages/tutorial.py", title="Tutorial"),
    st.Page("pages/dashboard.py", title="Dashboard"),
    st.Page("pages/console.py", title="Console (Interact with Docs)"),
    st.Page("pages/add_new_source.py", title="Add New Source"),
]

# Create navigation
pg = st.navigation(pages)



# Run the navigation
pg.run()