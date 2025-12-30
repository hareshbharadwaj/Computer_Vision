import cv2
image = cv2.imread(r"C:\Users\hesh2\OneDrive\Documents\viji-cv\sample_image.jpg")
flipped_image = cv2.flip(image, 1)
rotated_image = cv2.rotate(flipped_image, cv2.ROTATE_180)
cv2.imshow("Original Image", image)
cv2.imshow("Rotated 180-degree Clockwise Along Y-axis", rotated_image)
cv2.imwrite("rotated_image.jpg", rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()