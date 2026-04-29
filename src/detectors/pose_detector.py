import cv2
import mediapipe as mp

class Pose_Detector:
    def __init__(self):
        self.mp_pose = mp.solutions.pose
        self.mp_drawing = mp.solutions.drawing_utils

    def process(self, img):
        if img is None:
            raise ValueError("Imagem inválida")
        
        self.img = img
        self.img_width = img.shape[1]
        self.img_height = img.shape[0]

        with self.mp_pose.Pose(static_image_mode=True) as pose:
            img_cpy = self.img.copy()

            self.results = pose.process(img_cpy)
        
        return self.results
        
