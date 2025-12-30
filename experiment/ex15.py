import cv2
import numpy as np
# Read the input image
image = cv2.imread(r"C:\Users\hesh2\OneDrive\Documents\viji-cv\sample_image.jpg")  # Replace with your image file path
# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Convert to float32 for Harris Corner Detection
gray = np.float32(gray)
# Apply Harris Corner Detection
harris_corners = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)
# Dilate corner points for better visibility
harris_corners = cv2.dilate(harris_corners, None)
# Mark detected corners in red
image[harris_corners > 0.01 * harris_corners.max()] = [0, 0, 255]
# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Harris Corner Detection", image)
# Save the result
cv2.imwrite("harris_corners.jpg", image)
# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()