import streamlit as st
import cv2
import numpy as np
import tensorflow as tf
import json
import base64
from flask import Flask, request, jsonify

app = Flask(__name__)

def resize_image(image, target_size=(214, 214)):
    return cv2.resize(image, target_size, interpolation=cv2.INTER_LANCZOS4)

def canny_edge_detection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    return edges

def count_white_pixels(image):
    return np.sum(image == 255)

def handle_api_request():
    if request.method == "POST":
        data = request.get_json()
        base64_image = data.get('image', None)

        if base64_image:
            # Decode the base64 image and convert it to a bytes-like object
            image_data = base64.b64decode(base64_image)
            image = np.asarray(bytearray(image_data), dtype=np.uint8)
            original_image = cv2.imdecode(image, 1)

            # Resize the image to 214x214
            resized_image = resize_image(original_image, target_size=(214, 214))

            # Apply Canny edge detection to the resized image
            canny_image = canny_edge_detection(resized_image)

            # Calculate the sum of white pixels in the Canny image
            white_pixel_count = count_white_pixels(canny_image)

            # Prepare the response data
            response_data = {
                'original_image_size': original_image.shape,
                'canny_image_size': canny_image.shape,
                'white_pixel_count': white_pixel_count
            }

            # Return the response as JSON
            return jsonify(response_data)

        else:
            return jsonify({'error': 'Invalid JSON data. Image not found.'})

    else:
        return jsonify({'error': 'Invalid request method. Only POST method is supported.'})

@app.route('/api', methods=['POST'])
def api():
    return handle_api_request()

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
