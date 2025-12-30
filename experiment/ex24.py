import cv2
import numpy as np
# Read the image
image = cv2.imread(r"C:\Users\hesh2\OneDrive\Documents\viji-cv\sample_image.jpg", cv2.IMREAD_GRAYSCALE)  # Convert to grayscale while reading
# Define a kernel (5x5 structuring element)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
# Apply the Black Hat transformation
blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)
# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Black Hat Image", blackhat)
# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()