import numpy as np
import matplotlib.pyplot as plt
import random
import math

SIZE = 50  # 50 points


def linearRansac(xs, ys):
    iters = 10000
    aBest = 0
    bBest = 0
    pretotal = 0
    sigma = 0.2
    P = 0.99
    for i in range(iters):
        # choose random two point from original data xs
        x = xs[random.sample(range(len(xs)), 2)]
        y = ys[random.sample(range(len(ys)), 2)]
        a = (y[1] - y[0]) / (x[1] - x[0])
        b = y[1] - a * x[1]
        total_inlier = 0
        for j in range(len(xs)):
            y_estimate = a * xs[j] + b
            if abs(y_estimate - ys[j]) < sigma:
                total_inlier += 1

        if total_inlier > pretotal:
            iters = math.log(1 - P) / math.log(1 - math.pow(total_inlier / len(xs), 2))
            pretotal = total_inlier
            aBest = a
            bBest = b

        # Y = a * xs + b
        # loss = getLoss(ys, Y)
        # print("loss ", loss)  # 因为这里是随机两点，所以这个不算是loss

        if total_inlier > len(xs) * 0.995:
            break

    return aBest, bBest


def getLoss(yEstimates, yOris):
    loss = 0
    for i in range(len(yEstimates)):
        loss += math.pow((yEstimates[i] - yOris[i]), 2)
    return math.pow(loss, 1 / 2)


if __name__ == "__main__":
    xCords = []
    yCords = []
    for i in range(SIZE):
        x = 20 + random.random()
        y = 3 * x + random.random()
        xCords.append(x)
        yCords.append(y)

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title("RANSAC")
    xs = np.array(xCords)
    ys = np.array(yCords)
    ax1.scatter(xs, ys)
    a, b = linearRansac(xs, ys)
    Y = a * xs + b
    ax1.plot(xs, Y)
    plt.show()

