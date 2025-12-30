import cv2
import numpy as np


def add_text_to_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Could not load image")
        return

    text = input("Enter the text you want to add to the image: ")

    print("Enter the position coordinates for the text:")
    x = int(input("X coordinate: "))
    y = int(input("Y coordinate: "))

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    color = (255, 255, 255)
    thickness = 2

    img_with_text = cv2.putText(img, text, (x, y), font, font_scale, color, thickness)

    cv2.imshow('Image with Text', img_with_text)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    save = input("Do you want to save the image? (y/n): ")
    if save.lower() == 'y':
        output_path = input("Enter output file name (with extension): ")
        cv2.imwrite(output_path, img_with_text)
        print(f"Image saved as {output_path}")


if __name__ == "__main__":
    image_path = "sample_image.jpg"
    add_text_to_image(image_path)