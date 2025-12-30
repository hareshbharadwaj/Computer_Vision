import cv2
import numpy as np
image = cv2.imread(r"C:\Users\hesh2\OneDrive\Documents\viji-cv\sample_image.jpg")  # Replace 'image.jpg' with your image path
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
kernel = np.ones((5,5), np.uint8)
top_hat_image = cv2.morphologyEx(gray_image, cv2.MORPH_TOPHAT, kernel)
cv2.imshow('Original Image', image)
cv2.imshow('Top Hat Image', top_hat_image)
cv2.waitKey(0)
cv2.destroyAllWindows()