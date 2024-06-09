import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

# Create a file uploader component allowing the user to upload a file
uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")
    if camera_image:
        try:
            # Supply camera_image to convert_image to get the grayscale version
            img = Image.open(camera_image)
            gray_camera_img = img.convert('L')
            st.image(gray_camera_img)
        except Exception as e:
            st.error(f"Error processing camera image: {str(e)}")

# Check if the image exists meaning the user has uploaded a file
if uploaded_image:
    try:
        # Open the user uploaded image with PIL
        img = Image.open(uploaded_image)
        # Convert the image to grayscale
        gray_uploaded_img = img.convert('L')
        # Display the grayscale image on the webpage
        st.image(gray_uploaded_img)
    except Exception as e:
        st.error(f"Error processing uploaded image: {str(e)}")