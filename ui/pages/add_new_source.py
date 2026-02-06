import streamlit as st

# Initialize session state for the active source
if "active_source" not in st.session_state:
    st.session_state.active_source = None

# 1. Header & Official Icon Styles
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
            margin-top: -30px !important;
        }
        .gradient-text {
            font-size: 42px !important;
            font-weight: 700 !important;
            background: linear-gradient(90deg, #DC244C, #7B2FF7);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .subtitle-text { color: #94A3B8; font-size: 1.1rem; margin-bottom: 30px; }

        /* Card Container Styling */
        div.stButton > button {
            background: rgba(255, 255, 255, 0.03) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 16px !important;
            height: 180px !important;
            width: 100% !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            position: relative;
            overflow: hidden;
        }

        /* Hover State */
        div.stButton > button:hover {
            border-color: #DC244C !important;
            background: rgba(220, 36, 76, 0.1) !important;
            transform: translateY(-8px) !important;
            box-shadow: 0px 15px 30px rgba(0,0,0,0.5) !important;
        }

        /* Force image inside to follow hover */
        .icon-overlay {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            pointer-events: none; /* This allows mouse to click the button underneath */
            z-index: 10;
        }
            
    </style>
    
    <div style="margin-top: -30px;">
        <h1 class="gradient-text">Add New Source</h1>
        <p class="subtitle-text">Connect to official enterprise data streams.</p>
    </div>
""", unsafe_allow_html=True)

# 2. Updated Official Logo URLs
sources = [
    {"title": "PDF", "img": "https://upload.wikimedia.org/wikipedia/commons/8/87/PDF_file_icon.svg", "key": "pdf"},
    {"title": "Excel", "img": "https://cdn-icons-png.flaticon.com/512/732/732220.png", "key": "excel"},
    {"title": "PostgreSQL", "img": "https://upload.wikimedia.org/wikipedia/commons/2/29/Postgresql_elephant.svg", "key": "postgres"},
    {"title": "Google Drive", "img": "https://upload.wikimedia.org/wikipedia/commons/1/12/Google_Drive_icon_%282020%29.svg", "key": "gdrive"},
    {"title": "Amazon S3", "img": "https://upload.wikimedia.org/wikipedia/commons/b/bc/Amazon-S3-Logo.svg", "key": "s3"},
    {"title": "Azure Blob", "img": "https://www.vectorlogo.zone/logos/microsoft_azure/microsoft_azure-icon.svg", "key": "azure"},
    {"title": "GitHub", "img": "https://www.vectorlogo.zone/logos/github/github-icon.svg", "key": "github"},
    {"title": "ServiceNow", "img": "https://www.vectorlogo.zone/logos/servicenow/servicenow-icon.svg", "key": "snow"},
    {"title": "Confluence", "img": "https://cdn-icons-png.flaticon.com/512/5968/5968793.png", "key": "conf"}
]

# 3. Create the Grid
if st.session_state.active_source is None:
    cols = st.columns(3)
    for i, s in enumerate(sources):
        with cols[i % 3]:
            # Button is empty (no text)
            if st.button(" ", key=s['key'], use_container_width=True):
                st.session_state.active_source = s['key']
                st.rerun()
            
            # The Image Overlay - positioned exactly over the button
            st.markdown(
                f"""
                <div class="icon-overlay" style="margin-top: -115px;">
                    <img src="{s['img']}" width="80" style="filter: drop-shadow(0px 4px 8px rgba(0,0,0,0.2));">
                </div>
                """, 
                unsafe_allow_html=True
            )
else:
    # --- FORM VIEW ---
    selected = st.session_state.active_source

    if selected=="pdf" or selected=="excel":
        st.markdown(f"### Upload {selected.upper()} file ->")
        uploaded_files = st.file_uploader(
        "Choose files to index", 
        type=['pdf', 'csv', 'xlsx'], 
        accept_multiple_files=True
        )
        if uploaded_files:
            for file in uploaded_files:
                st.write(f"✅ Filename: {file.name}")

    if selected=="s3":
        # To read the file:
        st.markdown(f"### Add {selected.upper()} Connection")
        with st.form("connection_form"):
            col1, col2 = st.columns(2)
            with col1:
                st.text_input("Host / URL")
                st.text_input("Port")
            with col2:
                st.text_input("Access ID")
                st.text_input("Secret Key", type="password")
            if st.form_submit_button("Save Connection"):
                st.success(f"Connected to {selected}!")

    if st.button("← Back to Sources"):
        st.session_state.active_source = None
        st.rerun()