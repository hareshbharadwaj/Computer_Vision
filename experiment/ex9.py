import cv2
# Read the image
image = cv2.imread(r"C:\Users\hesh2\OneDrive\Documents\viji-cv\sample_image.jpg")  # Replace with your image file
# Resize to a bigger size (2x scaling)
bigger_image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
# Resize to a smaller size (0.5x scaling)
smaller_image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Bigger Image", bigger_image)
cv2.imshow("Smaller Image", smaller_image)
# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()