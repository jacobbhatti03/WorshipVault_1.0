import streamlit as st
from PIL import Image
import os
import io
import time

# ------------------------------------------------------------
# WorshipVault – Media Upload & Download App
# Version: 1.0  |  Author: Jacob Bhatti
# ------------------------------------------------------------

# 🔧 Streamlit configuration
st.set_page_config(
    page_title="WorshipVault",
    page_icon="✨",
    layout="wide"
)

# 🔧 Max upload limits
# (200 MB per file is Streamlit Cloud’s hard limit)
st.set_option("server.maxUploadSize", 200)
st.set_option("server.maxMessageSize", 400)

# ------------------------------------------------------------
# Paths and folders
UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Optional: Clean folder at every app restart
for f in os.listdir(UPLOAD_DIR):
    try:
        os.remove(os.path.join(UPLOAD_DIR, f))
    except Exception:
        pass

# ------------------------------------------------------------
# UI Header
st.title("✨ WorshipVault")
st.caption("Securely upload, view, and download your worship media files.")
st.divider()

# ------------------------------------------------------------
# Sidebar Info
st.sidebar.header("📁 App Settings")
st.sidebar.info(
    "• Max upload size: 200 MB per file\n"
    "• Supported: JPG, PNG, PDF\n"
    "• Auto-clears old uploads on restart"
)

# Placeholder for future Firebase toggle
use_firebase = st.sidebar.checkbox("Use Firebase Storage (coming soon)", value=False)

# ------------------------------------------------------------
# File Uploader
uploaded_files = st.file_uploader(
    "📤 Upload your worship images or PDFs",
    accept_multiple_files=True,
    type=["jpg", "jpeg", "png", "pdf"]
)

if uploaded_files:
    st.success(f"✅ {len(uploaded_files)} file(s) uploaded successfully!")

    for file in uploaded_files:
        file_path = os.path.join(UPLOAD_DIR, file.name)

        # Save file locally
        with open(file_path, "wb") as f:
            f.write(file.getbuffer())

        # Display image previews (for supported types)
        if file.type in ["image/png", "image/jpeg"]:
            img = Image.open(file)
            st.image(img, caption=file.name, use_container_width=True)
        else:
            st.write(f"📄 {file.name} (PDF file)")

        # Provide download link
        with open(file_path, "rb") as f:
            btn = st.download_button(
                label=f"⬇️ Download {file.name}",
                data=f,
                file_name=file.name,
                mime=file.type
            )

        st.divider()

# ------------------------------------------------------------
# Footer
st.markdown(
    """
    <div style="text-align:center; color:gray; margin-top:2rem;">
        WorshipVault © 2025 — Built with ❤️ using Streamlit  
        <br>Max upload 200 MB | Auto-clean enabled
    </div>
    """,
    unsafe_allow_html=True,
)
