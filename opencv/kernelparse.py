import cv2
import numpy as np

def parse_one_matrix(args_str):
    """
    assumes args_str is rows of numbers (i.e. matrix)
    ex:
        1 1 1 1
        1 1 1 1
        1 1 1 1
        1 1 1 1
    :param args_str: user string
    :return: convolution kernel as numpy array
    """
    rows = args_str.split('\n')
    height = len(rows)
    width = len(rows[0].split(' '))
    py_list = [[0]*width for _ in range(height)]
    for j in range(height):
        cols = rows[j].split(' ')
        for i in range(width):
            if i < len(cols):
                py_list[j][i] = parse_int(cols[i]) # 0 if bad value such as char

    nump_arr = np.asarray(py_list)
    return nump_arr


def parse_int(s):
    try:
        value = float(s)
        return value
    except ValueError:
        return 0