import cv2
import numpy as np


def cartoonify_image(image):
    # Convert the image to gray scale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a median blur to smooth the image
    gray = cv2.medianBlur(gray, 5)

    # Detect edges using adaptive thresholding
    edges = cv2.adaptiveThreshold(gray, 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 9)

    # Apply bilateral filter to reduce color palette
    color = cv2.bilateralFilter(image, 9, 300, 300)

    # Combine edges and colored image
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon


# Get the image path from user input
image_path = input("Enter the path to the image you want to cartoonify: ")

# Load the image
image = cv2.imread(image_path)

if image is None:
    print("Could not open or find the image. Please check the path.")
else:
    # Cartoonify the image
    cartoon_image = cartoonify_image(image)

    # Show the original and cartoonified images
    cv2.imshow('Original Image', image)
    cv2.imshow('Cartoon Image', cartoon_image)

    # Wait until a key is pressed and close the image windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
