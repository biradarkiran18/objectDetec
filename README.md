
# Real-Time Object Detection with YOLOv5

This project demonstrates how to perform real-time object detection using the YOLOv5 model with a Streamlit interface. You can use it to detect objects in both images and video streams (such as from a webcam). The model is pre-trained on the COCO dataset and can identify multiple objects like people, cars, animals, and more.

## Features
- **Image Detection**: Upload an image file (jpg, jpeg, png), and the app will detect objects in the image using YOLOv5.
- **Video Detection**: Real-time detection from a webcam feed with continuous object detection.

## Technologies Used
- **YOLOv5**: A state-of-the-art object detection model from the Ultralytics library.
- **Streamlit**: A simple web app framework for creating machine learning apps quickly.
- **OpenCV**: Used to process images and video streams.
- **PyTorch**: Used to load and run the YOLOv5 model.
- **PIL**: For handling image display in Streamlit.

## Installation

### Prerequisites
- Python 3.7+
- PyTorch and YOLOv5 dependencies

### Steps to Set Up:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/yolov5-streamlit-app.git
   cd yolov5-streamlit-app
   ```

2. **Install dependencies**:
   You can install the required dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:
   Start the app with the following command:
   ```bash
   streamlit run app.py
   ```

## Usage

### Image Detection:
1. Select **Image Detection** from the sidebar.
2. Upload an image by clicking **Browse files** or dragging an image into the file uploader.
3. The detected objects will be displayed with bounding boxes overlaid on the image.

### Video Detection:
1. Select **Video Detection** from the sidebar.
2. Check the **Run** checkbox to start real-time detection using your webcam.
3. Detected objects will be displayed on the video stream in real-time.

## Project Structure
- `app.py`: The main Streamlit app file.
- `requirements.txt`: List of required Python packages.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgements
- [YOLOv5 by Ultralytics](https://github.com/ultralytics/yolov5) for the object detection model.
- [Streamlit](https://streamlit.io) for the easy-to-use web application framework.
