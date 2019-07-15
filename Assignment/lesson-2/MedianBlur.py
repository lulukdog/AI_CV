import cv2
import numpy as np

PAD_WAY = {"ZERO": 0, "REPLICA": 1}


def medianFilter(img, kernelSize, padWay):
    imgPad = []
    if padWay == PAD_WAY["ZERO"]:
        imgPad = np.pad(img, (kernelSize - 2, kernelSize - 2), "constant")
    elif padWay == PAD_WAY["REPLICA"]:
        imgPad = np.pad(img, (kernelSize - 2, kernelSize - 2), "edge")

    rows, cols = img.shape
    res = np.zeros((rows, cols), dtype=img.dtype)
    for x in range(rows):
        for y in range(cols):
            mat = imgPad[x : x + kernelSize, y : y + kernelSize]
            res[x][y] = np.median(mat)
    return res


imgGray = cv2.imread("./lesson-2/noise.png", 0)
result = medianFilter(imgGray, 3, PAD_WAY["REPLICA"])
cv2.imshow("medianOut", result)
cv2.waitKey()
