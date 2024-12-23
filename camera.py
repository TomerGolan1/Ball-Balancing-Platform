import cv2
import numpy as np


class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)  
        # Check if the webcam is opened correctly
        if not self.cap.isOpened():
            print("Error: Could not open video device")
            exit()

    def __del__(self, x=0, y=0):
        # Release the webcam
        self.cap.release()

        
    def readAsGrayScaleMatrix(self):
        # Capture a single frame s
        ret, frame = self.cap.read()
        if not ret:
            print("Error: Could not read frame")
            exit()
        # Convert the image to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Convert the grayscale image to a numpy array (if needed)
        gray_matrix = np.array(gray_frame)
        return gray_matrix
        
        
# Print the grayscale matrix (optional)
#print(gray_matrix)
