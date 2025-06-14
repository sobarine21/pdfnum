import streamlit as st
import PyPDF2
import io

st.title("Multi-PDF Upload: Page Counter & Accurate PDF-to-Text Converter")

st.write(
    """
    Upload multiple PDF files. View the number of pages for each, and download the extracted text as `.txt` files.
    """
)

uploaded_files = st.file_uploader(
    "Choose PDF files", type=["pdf"], accept_multiple_files=True
)

if uploaded_files:
    st.header("PDF Summary & Text Download")
    for uploaded_file in uploaded_files:
        try:
            # Initialize PDF reader
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            num_pages = len(pdf_reader.pages)

            # Extract text from all pages
            extracted_text = ""
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    extracted_text += page_text + "\n"
                else:
                    extracted_text += "\n"  # For blank or unextractable pages

            # Prepare downloadable text file
            text_filename = uploaded_file.name.rsplit(".", 1)[0] + ".txt"
            text_bytes = extracted_text.encode("utf-8")
            text_io = io.BytesIO(text_bytes)

            # Show results
            st.success(f"**{uploaded_file.name}** — :page_facing_up: {num_pages} page(s)")
            st.download_button(
                label=f"Download extracted text for {uploaded_file.name}",
                data=text_io,
                file_name=text_filename,
                mime="text/plain",
            )

            # Optional: Show short preview of extracted text
            with st.expander(f"Preview text of {uploaded_file.name}"):
                st.text(extracted_text[:1500] + ("\n... (truncated)" if len(extracted_text) > 1500 else ""))

        except Exception as e:
            st.error(
                f"Could not process file `{uploaded_file.name}`. Error: {str(e)}"
            )
else:
    st.info("Upload one or more PDF files to get started.")

st.markdown("---")
st.caption("Built with Streamlit & PyPDF2")
