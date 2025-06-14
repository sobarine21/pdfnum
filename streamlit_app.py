import streamlit as st
import PyPDF2

st.title("Multi-PDF Upload & Page Counter App")

st.write(
    """
    Upload multiple PDF files. The app will display the number of pages for each PDF.
    """
)

uploaded_files = st.file_uploader(
    "Choose PDF files", type=["pdf"], accept_multiple_files=True
)

if uploaded_files:
    st.header("PDF Summary")
    for uploaded_file in uploaded_files:
        try:
            # file-like object for PyPDF2
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            num_pages = len(pdf_reader.pages)
            st.success(
                f"**{uploaded_file.name}** — :page_facing_up: {num_pages} page(s)"
            )
        except Exception as e:
            st.error(
                f"Could not process file `{uploaded_file.name}`. Error: {str(e)}"
            )
else:
    st.info("Upload one or more PDF files to get started.")

st.markdown("---")
st.caption("Built with Streamlit & PyPDF2")
