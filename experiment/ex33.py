import cv2
import numpy as np
def create_white_rectangle():
    width = int(input("Enter image width: "))
    height = int(input("Enter image height: "))

    white_image = np.ones((height, width, 3), np.uint8) * 255

    rect_width = width // 2
    rect_height = height // 2
    x = (width - rect_width) // 2
    y = (height - rect_height) // 2

    cv2.rectangle(white_image, (x, y), (x + rect_width, y + rect_height), (0, 0, 0), 2)

    cv2.imshow('White Image with Rectangle', white_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


create_white_rectangle()