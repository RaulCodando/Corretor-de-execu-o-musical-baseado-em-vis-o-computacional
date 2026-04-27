import cv2
import mediapipe as mp
import matplotlib.pyplot as plt

class Pose_Detector:
    def __init__(self, img):
        self.img = img
        self.img_width = img.shape[1]
        self.img_height = img.shape[0]

        self.fig, self.ax = plt.subplots(figsize = (10, 10))
        self.ax.axis("off")
        self.ax.imshow(img)
        plt.show()