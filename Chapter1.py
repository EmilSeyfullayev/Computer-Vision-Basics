import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)  # unsigned integers [0-255] eight bits

# importing image
# img = cv2.imread("Lenna_(test_image).png")
# cv2.imshow("Output", img)
# cv2.waitKey(0)

# importing video
# cap = cv2.VideoCapture('WhatsApp Video 2021-10-26 at 16.22.15.mp4')

# while True:
#     success, img = cap.read()
#     cv2.imshow("Output", img)
#
#     if cv2.waitKey(10) & 0xFF==ord('q'):
#         break

# webcam
# cap = cv2.VideoCapture(0)
# # cap.set(3, 640)
# # cap.set(4, 480)
# cap.set(10, 100)
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Output", img)
#     if cv2.waitKey(10) & 0xFF==ord('q'):
#         break

img = cv2.imread("Lenna_(test_image).png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0)
img_canny = cv2.Canny(img, 100, 100)
img_dilation = cv2.dilate(img_canny, kernel, iterations=1)
img_eroded = cv2.erode(img_dilation, kernel, iterations=1)

cv2.imshow("Canny", img_canny)
cv2.imshow("Dilation", img_dilation)
cv2.imshow("Eroded", img_eroded)
cv2.waitKey(0)
