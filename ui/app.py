import streamlit as st

# Set the page config (titles/icons)
st.set_page_config(page_title="EKIP", page_icon="📄", layout="wide")
st.sidebar.image(image="assets/logo.png")
# Define the pages and their icons/titles
pages = [
    st.Page("pages/welcome.py", title="Welcome", default=True),
    st.Page("pages/tutorial.py", title="Tutorial"),
    st.Page("pages/dashboard.py", title="Dashboard"),
    st.Page("pages/console.py", title="Console (Interact with Docs)"),
    st.Page("pages/add_new_source.py", title="Add New Source"),
    
]

# Create the navigation
pg = st.navigation(pages)

# --- Style Sidebar Navigation Titles ---
st.markdown("""
    <style>
            
       [data-testid="stLogo"] {
            height: 5rem !important; /* Increase from default small size */
            width: auto !important;
            margin-top: 15px !important;
            margin-left: 10px !important;
        }

        /* 2. Target the Image itself within the container */
        [data-testid="stLogo"] img {
            height: 60px !important; /* Adjust this value until it looks perfect */
            width: auto !important;
            object-fit: contain !important;
        }
        /* 1. Global Sidebar Background */
        [data-testid="stSidebar"] {
            background-color: #0D1117 !important;
            border-right: 2px solid #1E293B !important;
        }

        /* 1. Reset the header so we can see the border */
        header[data-testid="stHeader"] {
            visibility: visible !important;
            height: 3.5rem !important; /* Standard Streamlit header height */
            background-color: #0D1117 !important; /* Match your sidebar background */
            
            /* The Border between Header and Body */
            border-bottom: 1px solid #1E293B !important; 
            
            /* Optional: Add a slight shadow for depth */
            box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
        }
        
            
        /* 2. Style the Page Titles (The Text) */
        [data-testid="stSidebarNavItems"] span {
            font-size: 17px !important; /* Slightly smaller is often classier */
            font-weight: 500 !important;
            color: #8B949E !important; /* Elegant muted slate */
            font-family: 'Mono Sans', -apple-system, sans-serif;
            letter-spacing: -0.2px; /* Professional tight kerning */
            transition: all 0.3s ease;
        }

        /* 3. Style the Navigation Item Container */
        [data-testid="stSidebarNavItems"] li {
            margin-bottom: 4px !important;
            padding-left: 12px !important;
            padding-right: 12px !important;
        }

        /* 4. The Active Page Styling (Subtle & Modern) */
        /* Note: .st-emotion-cache classes change; targeting the 'active' state generically */
        [data-testid="stSidebarNavItems"] div[aria-selected="true"] {
            background-color: #1F2937 !important; /* Deep charcoal instead of red */
            border-radius: 8px !important; /* Rounded corners are essential for 'classy' */
            border-left: none !important; /* Remove the heavy bar */
        }

        [data-testid="stSidebarNavItems"] div[aria-selected="true"] span {
            color: #FFFFFF !important;
            font-weight: 800 !important;
        }

        /* 5. Hover Effect */
        [data-testid="stSidebarNavItems"] li:hover span {
            color: #F0F6FC !important;
        }
        
        [data-testid="stSidebarNavItems"] li:hover {
            background-color: rgba(255, 255, 255, 0.05) !important;
            border-radius: 8px !important;
        }

    </style>
    """, unsafe_allow_html=True)


# Run the navigation
pg.run()