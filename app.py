import streamlit as st
import cv2
import torch
from PIL import Image
import numpy as np
import tarfile

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

st.title("Real-Time Object Detection with YOLOv5")
st.sidebar.title("Select Mode")
option = st.sidebar.selectbox("Choose a detection mode", ("Image Detection", "Video Detection"))

if option == "Image Detection":
    st.subheader("Image-based Object Detection")
    
    # File uploader for image upload
    image_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if image_file is not None:
        # Convert image file to OpenCV format
        file_bytes = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
        frame = cv2.imdecode(file_bytes, 1)

        # Run YOLOv5 on the frame
        results = model(frame)

        # Render results
        frame = results.render()[0]

        # Display the image
        st.image(frame, channels="BGR", caption="Detection results")

elif option == "Video Detection":
    st.subheader("Real-Time Video Object Detection")
    
    run = st.checkbox('Run')

    if run:
        # Open the webcam
        cap = cv2.VideoCapture(0)
        stframe = st.empty()

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Run YOLOv5 on the frame
            results = model(frame)

            # Render the results
            frame = results.render()[0]

            # Convert frame to PIL format and display
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            stframe.image(frame)

        cap.release()

