from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image, UnidentifiedImageError
import pillow_heif  
from googletrans import Translator
import io

# Enable HEIC support
pillow_heif.register_heif_opener()

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



# Function to convert image format and handle MIME type
def convert_image_format(uploaded_file):
    try:
        image = Image.open(uploaded_file)
        buffer = io.BytesIO()
        image = image.convert("RGB")  # Ensure compatibility
        image.save(buffer, format="JPEG")
        buffer.seek(0)
        return buffer, "image/jpeg"
    except UnidentifiedImageError:
        raise ValueError("Unsupported image format. Please upload PNG, JPEG, or HEIC images.")

# Function to load Google Gemini Pro Vision API and get response
def get_gemini_response(input, image_data, mime_type, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([
        {"mime_type": mime_type, "data": image_data},
        input,
        prompt,
    ])
    return response.text

# Function to prepare image data
def input_image_setup(uploaded_file):
    converted_file, mime_type = convert_image_format(uploaded_file)
    bytes_data = converted_file.getvalue()
    return bytes_data, mime_type

# Translation function using googletrans
def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

# Initialize Streamlit app
st.set_page_config(page_title="Food Locha")

st.title("Food Locha: Made with ❣️")
st.text("       - Developed By: Mohammad Ayaz Alam")
st.header("Upload your meal image to get the calorie details")

# Input and file uploader
input = st.text_input("Ask Specific Question: (Optional)", key="input")
uploaded_file = st.file_uploader("Choose an image...")

if uploaded_file:
    try:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_container_width=True)
    except UnidentifiedImageError:
        st.error("Unsupported image format. Please upload PNG, JPEG, or HEIC images.")

# Language selection dropdown
language_map = {"English": "en", "French": "fr", "Dutch": "nl", "German": "de"}
selected_language = st.selectbox(
    "Select the language for the output:", options=list(language_map.keys())
)

# Submit button
submit = st.button("Tell me the total calories")

# Input prompt
input_prompt = """
You are an expert nutritionist. Your task is to identify the food items from the image provided, calculate the total calories, 
and provide details for each food item in the following format. Do not include disclaimers or mention whether the counts are estimated or exact. Focus only on the calorie count and suggestions.

               1. Item 1 - no of calories
               2. Item 2 - no of calories
               ----
               ----

               Suggestion:
                    1. Suggestion 1: ---------
                    2. Suggestion 2: ---------
"""

# If submit button is clicked
if submit:
    if uploaded_file:
        with st.spinner("Processing... Please wait."):
            try:
                # Prepare image data
                image_data, mime_type = input_image_setup(uploaded_file)

                # Get Gemini response
                response = get_gemini_response(input, image_data, mime_type, input_prompt)

                # Translate the response to the selected language
                target_language = language_map[selected_language]
                translated_response = translate_text(response, target_language)

                # Display the translated response
                st.subheader(f"The Response in {selected_language} is:")
                st.write(translated_response)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please upload an image to proceed.")
