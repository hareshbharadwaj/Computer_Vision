import cv2
import numpy as np


def subtract_foreground(image_path, lower_threshold, upper_threshold):
    """
    Subtract foreground from image based on color thresholds

    Args:
        image_path: Path to the input image
        lower_threshold: List of [H, S, V] values for lower bound
        upper_threshold: List of [H, S, V] values for upper bound

    Returns:
        Mask of the foreground and the result image
    """
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Could not read the image")
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower = np.array(lower_threshold)
    upper = np.array(upper_threshold)

    mask = cv2.inRange(hsv, lower, upper)

    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    result = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(mask))

    return mask, result


if __name__ == "__main__":
    lower_green = [35, 50, 50]
    upper_green = [85, 255, 255]

    mask, result = subtract_foreground('sample_image.jpg', lower_green, upper_green)

    cv2.imshow('Original', cv2.imread('sample_image.jpg'))
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()