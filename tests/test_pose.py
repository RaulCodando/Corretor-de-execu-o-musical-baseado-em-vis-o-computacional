from src.detectors.pose_detector import Pose_Detector
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("tests/samples/pose/dom-hill-nimElTcTNyY-unsplash.jpg")

detector = Pose_Detector()
detector.process(img)

fig, ax = plt.subplots(figsize = (10, 10))
ax.axis("off")
ax.imshow(img[...,::-1])
plt.show()