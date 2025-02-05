import cv2
from PIL import Image
import numpy as np
import time

PATH_IMG1 = "./cam1.png"
PATH_IMG2 = "./cam2.png"


def closest_color(color):
    # colors = {
    #     [255, 0, 0]: "R",
    #     [0, 255, 0]: "F",
    #     [0, 0, 0]: "U",
    #     [0, 0, 255]: "B",
    #     [255, 100, 0]: "L",
    #     [255, 255, 0]: "D",
    # }

    color_keys = np.array(
        [
            [255, 0, 0],
            [0, 255, 0],
            [255, 255, 255],
            [0, 0, 255],
            [255, 100, 0],
            [255, 255, 0],
        ]
    )
    colors = ["L", "F", "U", "B", "L", "D"]
    color = np.array(color)

    distances = np.sqrt(np.sum((color_keys - color) ** 2, axis=1))
    print(color)
    print(distances)
    index_of_smallest = np.argmin(distances)
    smallest_distance = colors[index_of_smallest]
    return smallest_distance


def take_images():
    cam1 = cv2.VideoCapture(0)
    cam1.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cam1.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    time.sleep(1.5)

    r, i = cam1.read()
    cam1.release()

    cv2.imshow("Nice", i)
    cv2.waitKey(0)
    cv2.destroyWindow("Nice")
    cv2.imwrite(PATH_IMG1, i)

    cam2 = cv2.VideoCapture(1)
    cam2.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cam2.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    time.sleep(1.5)

    r, i = cam2.read()
    cam2.release()

    cv2.imshow("Nice", i)
    cv2.destroyWindow("Nice")
    cv2.imwrite(PATH_IMG2, i)


def process_cam1():
    img = Image.open(PATH_IMG1)
    pixels = img.load()

    U = []
    R = []
    F = []

    U.append(closest_color(pixels[x, y]))
    U.append(closest_color(pixels[x, y]))
    U.append(closest_color(pixels[x, y]))
    U.append(closest_color(pixels[x, y]))
    U.append(closest_color(pixels[x, y]))
    U.append(closest_color(pixels[x, y]))
    U.append(closest_color(pixels[x, y]))
    U.append(closest_color(pixels[x, y]))
    U.append(closest_color(pixels[x, y]))

    R.append(closest_color(pixels[x, y]))
    R.append(closest_color(pixels[x, y]))
    R.append(closest_color(pixels[x, y]))
    R.append(closest_color(pixels[x, y]))
    R.append(closest_color(pixels[x, y]))
    R.append(closest_color(pixels[x, y]))
    R.append(closest_color(pixels[x, y]))
    R.append(closest_color(pixels[x, y]))
    R.append(closest_color(pixels[x, y]))

    F.append(closest_color(pixels[x, y]))
    F.append(closest_color(pixels[x, y]))
    F.append(closest_color(pixels[x, y]))
    F.append(closest_color(pixels[x, y]))
    F.append(closest_color(pixels[x, y]))
    F.append(closest_color(pixels[x, y]))
    F.append(closest_color(pixels[x, y]))
    F.append(closest_color(pixels[x, y]))
    F.append(closest_color(pixels[x, y]))

    print("process")
    return U, R, F


def process_cam2():
    img2 = Image.open(PATH_IMG2)
    pixels = img2.load()

    B = []
    L = []
    D = []

    B.append(closest_color(pixels[x, y]))
    B.append(closest_color(pixels[x, y]))
    B.append(closest_color(pixels[x, y]))
    B.append(closest_color(pixels[x, y]))
    B.append(closest_color(pixels[x, y]))
    B.append(closest_color(pixels[x, y]))
    B.append(closest_color(pixels[x, y]))
    B.append(closest_color(pixels[x, y]))
    B.append(closest_color(pixels[x, y]))

    L.append(closest_color(pixels[x, y]))
    L.append(closest_color(pixels[x, y]))
    L.append(closest_color(pixels[x, y]))
    L.append(closest_color(pixels[x, y]))
    L.append(closest_color(pixels[x, y]))
    L.append(closest_color(pixels[x, y]))
    L.append(closest_color(pixels[x, y]))
    L.append(closest_color(pixels[x, y]))
    L.append(closest_color(pixels[x, y]))

    D.append(closest_color(pixels[x, y]))
    D.append(closest_color(pixels[x, y]))
    D.append(closest_color(pixels[x, y]))
    D.append(closest_color(pixels[x, y]))
    D.append(closest_color(pixels[x, y]))
    D.append(closest_color(pixels[x, y]))
    D.append(closest_color(pixels[x, y]))
    D.append(closest_color(pixels[x, y]))
    D.append(closest_color(pixels[x, y]))

    return B, L, D


def process():
    U, R, F = process_cam1()
    B, L, D = process_cam2()
    return "".join(U) + "".join(R) + "".join(F) + "".join(B) + "".join(L) + "".join(D)


def koc_to_anim(string):
    res = (
        string[6]
        + string[7]
        + string[8]
        + string[3]
        + string[4]
        + string[5]
        + string[0]
        + string[1]
        + string[2]
    )
    res += (
        string[27]
        + string[30]
        + string[33]
        + string[28]
        + string[31]
        + string[34]
        + string[29]
        + string[32]
        + string[35]
    )
    res += (
        string[18]
        + string[21]
        + string[24]
        + string[19]
        + string[22]
        + string[25]
        + string[20]
        + string[23]
        + string[26]
    )
    res += (
        string[45]
        + string[48]
        + string[51]
        + string[46]
        + string[49]
        + string[52]
        + string[47]
        + string[50]
        + string[53]
    )
    res += (
        string[38]
        + string[37]
        + string[36]
        + string[41]
        + string[40]
        + string[39]
        + string[44]
        + string[43]
        + string[42]
    )
    res += (
        string[9]
        + string[12]
        + string[15]
        + string[10]
        + string[13]
        + string[16]
        + string[11]
        + string[14]
        + string[17]
    )
    return res
