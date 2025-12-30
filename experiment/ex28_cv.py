import cv2

# Load the pre-trained Haar cascade for cars
car_cascade = cv2.CascadeClassifier("cars.xml")  # Make sure this file is in the same directory

# Load the video file (or use '0' for webcam)
video = cv2.VideoCapture("traffic.mp4")  # Replace with your video file path

# Check if video opened successfully
if not video.isOpened():
    print("Error: Could not open video.")
    exit()

# Process video frame-by-frame
while True:
    ret, frame = video.read()
    if not ret:
        break  # End of video

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect vehicles
    cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(50, 50))

    # Draw rectangles around detected vehicles
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Vehicle", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Show the frame
    cv2.imshow("Vehicle Detection", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
video.release()
cv2.destroyAllWindows()
