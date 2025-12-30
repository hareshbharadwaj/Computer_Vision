import numpy as np
import cv2
def create_image_with_boxes():
    size = int(input("Enter the size of the square image (pixels): "))

    img = np.ones((size, size, 3), dtype=np.uint8) * 255

    box_size = size // 10

    img[0:box_size, 0:box_size] = [0, 0, 0]

    img[0:box_size, -box_size:] = [255, 0, 0]

    img[-box_size:, 0:box_size] = [0, 255, 0]

    img[-box_size:, -box_size:] = [0, 0, 255]

    cv2.imshow('Image with Colored Boxes', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    create_image_with_boxes()