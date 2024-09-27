import torch
from transformers import VisionEncoderDecoderModel, AutoTokenizer
from PIL import Image
import streamlit as st

# Load the GOT model and tokenizer
model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Function to load and preprocess the image
def load_image(image_path):
    image = Image.open(image_path).convert("RGB")
    return image

# Function to perform OCR using the GOT model
def ocr_image(image):
    # Preprocess and convert the image for the model
    pixel_values = tokenizer(image, return_tensors="pt").pixel_values
    pixel_values = pixel_values.to(device)

    # Generate the OCR text
    outputs = model.generate(pixel_values)
    text = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
    return text

# Streamlit web app for image upload and OCR processing
st.title("OCR Web App - General OCR Theory Model")
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
        highlighted_text = extracted_text.replace(keyword, f"**{keyword}**")
        st.write(highlighted_text)


