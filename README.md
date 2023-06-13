# Vehicle_Tracking_Counting

# YOLONAS Vehicle Tracking and Counting

## Overview
YOLONAS Vehicle Tracking and Counting is a software application that utilizes the YOLO (You Only Look Once) object detection algorithm to track and count vehicles in video streams or recorded videos. This README provides a simple guide to help you understand and use the YOLONAS application.

## Features
- Vehicle detection: The application uses the YOLO algorithm to identify and track vehicles in video frames.
- Real-time tracking: YOLONAS provides real-time tracking of vehicles, allowing you to monitor and count vehicles as they move within the video stream.
- Vehicle counting: The software accurately counts the number of vehicles detected within the specified video or video stream.
- Easy configuration: YOLONAS offers simple configuration options to adjust detection thresholds, input video sources, and output settings.

## Requirements
- Python 3.x
- OpenCV library
- YOLOv3 pre-trained weights (already included in the repository)
- CUDA (optional for GPU acceleration)

## Installation
1. Clone the YOLONAS repository to your local machine.
2. Install the required dependencies, including Python 3.x and OpenCV. You can use pip to install the necessary packages by running the following command:


Replace `<input_video_path>` with the path to the video file you want to analyze.
3. The application will process the video frames, track the vehicles, and display the count in the terminal.

## Configuration
You can modify certain parameters to customize the behavior of YOLONAS:
- `--input`: Specifies the path to the input video file or video stream.
- `--output`: (Optional) Specifies the path to save the processed video with bounding boxes (default: `output.mp4`).
- `--confidence`: (Optional) Sets the minimum confidence threshold for vehicle detection (default: 0.5).
- `--threshold`: (Optional) Sets the non-maximum suppression threshold to filter overlapping bounding boxes (default: 0.3).
- `--gpu`: (Optional) Enables GPU acceleration if CUDA is installed and available.

