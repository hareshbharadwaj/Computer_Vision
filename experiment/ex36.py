import cv2
import numpy as np


def subtract_background_color(image_path, lower_color, upper_color):
    """
    Subtract background based on color range

    Args:
        image_path: Path to the input image
        lower_color: Array of lower HSV values [H, S, V]
        upper_color: Array of upper HSV values [H, S, V]

    Returns:
        Masked image with background removed
    """
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Could not read the image")

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower = np.array(lower_color)
    upper = np.array(upper_color)
    mask = cv2.inRange(hsv, lower, upper)

    mask = cv2.bitwise_not(mask)

    result = cv2.bitwise_and(image, image, mask=mask)

    return result


if __name__ == "__main__":
    lower_color = [0, 0, 200]
    upper_color = [180, 30, 255]

    result = subtract_background_color('sample_image.jpg', lower_color, upper_color)

    cv2.imshow('Result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()