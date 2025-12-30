import cv2

# Load image
image = cv2.imread(r"C:\Users\hesh2\OneDrive\Documents\viji-cv\sample_watch_image.jpg")  # Change filename as needed
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Preprocessing
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 50, 150)

# Find contours
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Loop through contours to find possible watch
for cnt in contours:
    area = cv2.contourArea(cnt)
    if 1000 < area < 10000:  # Adjust area thresholds
        x, y, w, h = cv2.boundingRect(cnt)
        aspect_ratio = w / float(h)

        # Assuming watch is roughly square or rectangular
        if 0.7 < aspect_ratio < 1.3:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, "Watch?", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

# Show result
cv2.imshow("Watch Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
