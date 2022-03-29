import cv2

img = cv2.imread("Lenna_(test_image).png")

img_resized = cv2.resize(img, (200, 200))
print(f'Original image shape {img.shape}')
print(f'Resized image shape {img_resized.shape}')

img_cropped = img[0:200, 0:200]
cv2.imshow('Resized', img_resized)
cv2.imshow('Cropped', img_cropped)
cv2.waitKey(0)