import cv2
import streamlit as st
import numpy as np

def canny_edge_detection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    return edges

def resize_image(image, width, height):
    return cv2.resize(image, (width, height))

def main():
    st.title("Canny Edge Detection with Image Resizing")
    
    # Capture image from the webcam
    cap = cv2.VideoCapture(0)
    st.write("Press 'Capture' to take a picture.")
    
    if st.button("Capture"):
        ret, frame = cap.read()
        if ret:
            st.image(frame, channels="BGR", caption="Captured Image")
            
            # Perform Canny edge detection
            edges = canny_edge_detection(frame)
            st.image(edges, caption="Canny Edge Detection")
            
            # Resize the image to 214x214 pixels
            resized_image = resize_image(frame, 214, 214)
            st.image(resized_image, channels="BGR", caption="Resized Image (214x214)")
        
        cap.release()
    
if __name__ == "__main__":
    main()
