import cv2

def segment_image(image_path, lower_threshold=127, upper_threshold=255):
    image = cv2.imread(image_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, binary = cv2.threshold(gray, lower_threshold, upper_threshold, cv2.THRESH_BINARY)

    _, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY, 11, 2)

    cv2.imshow('Original', image)
    cv2.imshow('Binary Segmentation', binary)
    cv2.imshow('Otsu Segmentation', otsu)
    cv2.imshow('Adaptive Segmentation', adaptive)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    image_path = 'face_image.jpg'

    segment_image(image_path)

    # segment_image(image_path, 100, 255)