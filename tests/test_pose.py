from src.detectors.pose_detector import Pose_Detector
import cv2

img = cv2.imread("tests/samples/pose/dom-hill-nimElTcTNyY-unsplash.jpg")

poseDetector = Pose_Detector(img)