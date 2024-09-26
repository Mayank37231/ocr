import re

import pytesseract
import streamlit as st
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to extract text from image
def extract_text_from_image(image):
    img = Image.open(image)
    text = pytesseract.image_to_string(img, lang='eng+hin')  # OCR for English and Hindi
    return text

# Function to highlight keyword matches in the extracted text
def highlight_keywords(text, keyword):
    highlighted_text = re.sub(f'({keyword})', r'**\1**', text, flags=re.IGNORECASE)
    return highlighted_text

# Streamlit UI
st.title("OCR Image Text Extraction & Keyword Search")
st.write("Upload an image containing text, extract the text, and search for specific keywords.")

# Step 1: Image Upload
uploaded_image = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])

if uploaded_image is not None:
    # Step 2: Extract text from the uploaded image
    with st.spinner("Extracting text..."):
        extracted_text = extract_text_from_image(uploaded_image)
    st.write("### Extracted Text")
    st.text_area("Extracted Text", extracted_text, height=300)

    # Step 3: Keyword Search
    st.write("### Search within Extracted Text")
    search_keyword = st.text_input("Enter a keyword to search for:")

    if search_keyword:
        # Highlighting the matches in the extracted text
        highlighted_text = highlight_keywords(extracted_text, search_keyword)
        st.write("### Search Results (Highlighted Matches)")
        st.markdown(highlighted_text, unsafe_allow_html=True)

