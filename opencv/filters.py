import cv2
import numpy as np

def convolve(img, kernel):
    dst = cv2.filter2D(img,-1,kernel)
    return dst


def edge(img, kern_dim):
    if not kern_dim:
        kern_dim = 5

    kernel = np.asarray([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) / 5

    centre = [[0] * kern_dim for _ in range(kern_dim)]
    centre[kern_dim // 2][kern_dim // 2] = 5

    kernel = np.asarray(centre) - kernel

    dst = convolve(img, kernel)

    return dst

