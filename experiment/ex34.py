import cv2
import numpy as np


def create_circle_image(width, height, circle_radius=None):
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    center_x = width // 2
    center_y = height // 2
    if circle_radius is None:
        circle_radius = min(width, height) // 4

    cv2.circle(image, (center_x, center_y), circle_radius, (0, 0, 0), 2)

    return image


def main():
    width = int(input("Enter image width: "))
    height = int(input("Enter image height: "))

    result = create_circle_image(width, height)

    cv2.imshow('White Image with Circle', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()