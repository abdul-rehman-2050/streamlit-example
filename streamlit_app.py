import streamlit as st
import cv2
import numpy as np
import tensorflow as tf

def resize_image(image, target_size=(214, 214)):
    return cv2.resize(image, target_size, interpolation=cv2.INTER_LANCZOS4)

def canny_edge_detection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    return edges

def main():
    st.title("Image Resizer and Canny Edge Detection")

    # File uploader widget to upload an image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Read the uploaded image
        image_data = uploaded_file.read()
        image = np.asarray(bytearray(image_data), dtype=np.uint8)
        original_image = cv2.imdecode(image, 1)

        # Resize the image
        resized_image = resize_image(original_image)

        # Apply Canny edge detection to the resized image
        canny_image = canny_edge_detection(resized_image)

        # Display the original and Canny images side by side
        st.image([original_image, canny_image], caption=["Original Image", "Canny Edge Detection"], use_column_width=True)

if __name__ == "__main__":
    main()
