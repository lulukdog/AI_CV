import cv2
import random
import numpy as np

PICPATH = []
for i in range(1,21):
    PICPATH.append('./img/0_' + str(i) + '.jpg')


imagePath = PICPATH[random.randint(0,len(PICPATH)-1)]
##############################
# img_gray = cv2.imread('./lenna.png', 0)
# cv2.imshow('lenna_gray', img_gray)
# key = cv2.waitKey()
# if key == 27:
#     cv2.destroyWindow('lenna')

# # to show gray image to show image matrix
# print('image pixel array:\n',img_gray)

# # to show image data type
# print('\nimage data type:',img_gray.dtype)

# # to show gray image shape
# print('\nimage (height,width) is:',img_gray.shape)  # h, w

##############################
# original image color
img = cv2.imread(imagePath)
# cv2.imshow('lenna',img)
# key = cv2.waitKey()
# if key == 27:
#     cv2.destroyAllWindows()

# print('color image pixel array:\n',img)
# print('\nimage (height,width,color_dim) is:',img.shape)  # h,w,c

##############################
# image crop
# img_crop = img[200:400,100:400]
# cv2.imshow('lenna_crop',img_crop)
# key = cv2.waitKey()
# if key == 27:
#     cv2.destroyAllWindows()

##############################
# image split
# B,G,R = cv2.split(img)
# cv2.imshow('R',R)
# cv2.moveWindow('R',100,100)
# cv2.imshow('G',G)
# cv2.moveWindow('G',100+img.shape[1]+20,100)
# cv2.imshow('B',B)
# cv2.moveWindow('B',100+(img.shape[1]+20)*2,100)
# print('R',R)
# print('G',G)
# print('B',B)
# key = cv2.waitKey()
# if key == 27:
#     cv2.destroyAllWindows()

##############################
# def lightImg(image):
# 	r_rand = random.randint(1,50)
# 	lim = 255 - r_rand
# 	R[R > lim] = 255
# 	R[R <= lim] = (r_rand + R[R <= lim]).astype(img.dtype)

# 	g_rand = random.randint(1,50)
# 	lim = 255 - g_rand
# 	G[G > lim] = 255
# 	G[G <= lim] = (g_rand + G[G <= lim]).astype(img.dtype)

# 	b_rand = random.randint(1,50)
# 	lim = 255 - b_rand
# 	B[B > lim] = 255
# 	B[B <= lim] = (b_rand + B[B <= lim]).astype(img.dtype)

# 	imgMerge = cv2.merge((B, G, R))
# 	return imgMerge

# img_random_color = lightImg(img)
# cv2.imshow('img_random_color', img_random_color)
# key = cv2.waitKey()
# if key == 27:
#     cv2.destroyAllWindows()

##############################
# Affine Transform
# rows, cols, ch = img.shape
# pts1 = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1]])
# pts2 = np.float32([[cols * 0.2, rows * 0.1], [cols * 0.9, rows * 0.2], [cols * 0.1, rows * 0.9]])
# ## 3 point not in one line can confirm a plane
# M = cv2.getAffineTransform(pts1, pts2)
# dst = cv2.warpAffine(img, M, (cols, rows))
# cv2.imshow('affine lenna', dst)
# key = cv2.waitKey()
# if key == 27:
#     cv2.destroyAllWindows()

############################
# perspective transform
def random_warp(img, row, col):
    height, width, channels = img.shape

    # warp:
    random_margin = 60
    x1 = random.randint(-random_margin, random_margin)
    y1 = random.randint(-random_margin, random_margin)
    x2 = random.randint(width - random_margin - 1, width - 1)
    y2 = random.randint(-random_margin, random_margin)
    x3 = random.randint(width - random_margin - 1, width - 1)
    y3 = random.randint(height - random_margin - 1, height - 1)
    x4 = random.randint(-random_margin, random_margin)
    y4 = random.randint(height - random_margin - 1, height - 1)

    dx1 = random.randint(-random_margin, random_margin)
    dy1 = random.randint(-random_margin, random_margin)
    dx2 = random.randint(width - random_margin - 1, width - 1)
    dy2 = random.randint(-random_margin, random_margin)
    dx3 = random.randint(width - random_margin - 1, width - 1)
    dy3 = random.randint(height - random_margin - 1, height - 1)
    dx4 = random.randint(-random_margin, random_margin)
    dy4 = random.randint(height - random_margin - 1, height - 1)

    pts1 = np.float32([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
    pts2 = np.float32([[dx1, dy1], [dx2, dy2], [dx3, dy3], [dx4, dy4]])
    M_warp = cv2.getPerspectiveTransform(pts1, pts2)
    img_warp = cv2.warpPerspective(img, M_warp, (width, height))
    return M_warp, img_warp
M_warp, img_warp = random_warp(img, img.shape[0], img.shape[1])
cv2.imshow('lenna_warp', img_warp)
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
