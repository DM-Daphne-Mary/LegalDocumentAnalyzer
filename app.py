
import streamlit as st
from document_processor import extract_text_from_pdf

# Page configuration
st.set_page_config(
    page_title="Legal Document Analyzer",
    page_icon="⚖️",
    layout="wide"
)

# Custom design
st.markdown("""
<style>
.stApp {
    background-color: #101525;
    color: white;
}

.main-title {
    text-align: center;
    color: #a78bfa;
    font-size: 38px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    font-size: 17px;
}

.stButton button {
    background: #7654e8;
    color: white;
    border-radius: 10px;
    border: none;
    height: 45px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# Header
st.markdown(
    '<div class="main-title">⚖️ Legal Document Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-Powered Legal Document Analysis</div>',
    unsafe_allow_html=True
)

st.divider()

# Introduction
st.header("📄 Upload Your Legal Document")

st.write(
    "Upload a PDF document to extract its text "
    "and analyze important legal information."
)

# PDF uploader
uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("Document uploaded successfully!")

    if st.button("Extract Document Text"):

        with st.spinner("Extracting text..."):

            extracted_text = extract_text_from_pdf(uploaded_file)

        if extracted_text.startswith("Error"):
            st.error(extracted_text)

        elif extracted_text == "No readable text found in this PDF.":
            st.warning(extracted_text)

        else:
            st.success("Text extracted successfully!")

            st.subheader("📑 Extracted Document Content")

            st.text_area(
                "Document Text",
                extracted_text,
                height=300
            )

st.divider()

st.info(
    "Next: AI will analyze the document and identify "
    "important clauses, payment terms, obligations and dates."
)

st.caption("Legal Document Analyzer | Built using Python and Streamlit")
