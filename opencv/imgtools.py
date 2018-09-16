import cv2



def write_image(img, server_id, filename_prefix):
    cv2.imwrite('data\databases\{}\output\images\output_{}.png'.format(server_id, filename_prefix), img)
