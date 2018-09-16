import numpy as np
import cv2
import random


#b,g,r = cv2.split(img)
#img = cv2.merge((r,b,g))
# img[:,:,2] = (img[i,j,2] for i in range(img.shape[0]) for j in range(img.shape[1]))
#img[:,:] = [random.randrange(255),random.randrange(255),random.randrange(255)]
# for i in range(img.shape[0]):
#     for j in range(img.shape[1]):
#         img[i,j] = [random.randrange(255),random.randrange(255),random.randrange(255)]
# eye = img[320:350, 330:400]
# img[300:330, 150:220] = eye

img1 = cv2.imread("00_cover.jpg")
img2 = cv2.imread('grill.png')

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()



#cv2.imshow('image',img1)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('untitled.png',img1)
    cv2.destroyAllWindows()