import cv2


def read_image(filename):
    img = cv2.imread(filename)
    return img