import streamlit as st
from datetime import datetime

# Page Config
st.set_page_config(page_title="WorshipVault", page_icon="🙏", layout="wide")

# Header Section
st.markdown("""
    <div style='text-align: center;'>
        <h1>🙏 WorshipVault</h1>
        <h4>Share and download worship media files with your community.</h4>
    </div>
    <hr>
""", unsafe_allow_html=True)

# Upload Section
st.subheader("📤 Upload Your File")
uploaded_file = st.file_uploader("Select image or PDF", type=["jpg", "jpeg", "png", "pdf"])

if uploaded_file:
    # Display file name and download option
    st.success(f"✅ '{uploaded_file.name}' uploaded successfully!")
    st.download_button(
        label="⬇️ Download This File",
        data=uploaded_file,
        file_name=uploaded_file.name,
        mime="application/octet-stream"
    )

# Divider
st.divider()

# About Section
st.markdown("""
### 🌍 About WorshipVault
WorshipVault is a shared media cloud app designed for worship teams, churches, and creators to 
upload, access, and download worship images, lyric slides, and PDFs — all in one place.

🚧 *Next update: Cloud storage + login system with Firebase integration.*
""")
