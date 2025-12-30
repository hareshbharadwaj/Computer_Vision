import cv2
image = cv2.imread(r"C:\Users\hesh2\OneDrive\Documents\viji-cv\sample_image.jpg")  # Replace with your image file
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray_image, 100, 200)  # 100 and 200 are threshold values
cv2.imshow("Original Image", image)
cv2.imshow("Edge Detected Image", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()