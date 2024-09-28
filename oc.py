import pytesseract
from PIL import Image
import streamlit as st
import os

# Set the path for the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'

# Function to load and preprocess the image
def load_image(image_path):
    image = Image.open(image_path).convert("RGB")
    return image

# Function to perform OCR using Tesseract
def ocr_image(image):
    # Perform OCR using pytesseract
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text

# Streamlit web app for image upload and OCR processing
st.title("OCR Web App - Tesseract OCR")
uploaded_image = st.file_uploader("Upload an Image", type=['jpeg', 'png', 'jpg'])

if uploaded_image is not None:
    image = load_image(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    extracted_text = ocr_image(image)
    st.write("**Extracted Text:**")
    st.write(extracted_text)

    # Keyword search
    keyword = st.text_input("Enter a keyword to search:")
    if keyword:
        # Convert both keyword and text to lowercase for case-insensitive search
        extracted_text_lower = extracted_text.lower()
        keyword_lower = keyword.lower()

        # Highlight all occurrences of the keyword (case-insensitive)
        highlighted_text = extracted_text_lower.replace(keyword_lower, f"**{keyword}**")
        
        # Display the result
        st.write(highlighted_text)
