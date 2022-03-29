import cv2
import numpy as np

image = np.zeros((512, 512, 3), np.uint8)

# image[50:100, 50:100] = 255, 0, 0 # rectangle is blue
# image[:] = 255, 0, 0 # all image is blue

cv2.line(image, (0,0), (512, 512), (0, 255, 0), 3)
cv2.rectangle(image, (100, 100), (250, 250), (0, 0, 255), 3)
# cv2.rectangle(image, (100, 100), (250, 250), (0, 0, 255), cv2.FILLED)
cv2.circle(image, (400, 100), 30, (123, 123, 123), 2)
cv2.putText(image, "OpenCV", (200, 400), cv2.FONT_ITALIC, 1, (255, 255, 255), 2)



cv2.imshow("Output", image)
cv2.waitKey(0)