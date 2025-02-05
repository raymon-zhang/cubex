import cv2
from PIL import Image
import numpy as np
import time

PATH_IMG1 = "./cam1.png"
PATH_IMG2 = "./cam2.png"

x=0
y=0


def closest_color(color):
    # colors = {
    #     [255, 0, 0]: "R",
    #     [0, 255, 0]: "F",
    #     [0, 0, 0]: "U",
    #     [0, 0, 255]: "B",
    #     [255, 100, 0]: "L",
    #     [255, 255, 0]: "D",
    # }

    color_keys =  np.array([
        [255, 0, 0],
        [0, 255, 0],
        [255, 255, 255],
        [0, 0, 255],
        [255, 100, 0],
        [255, 255, 0],
    ])
    colors=["L", "F", "U", "B", "L", "D"]
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


    # cam2 = cv2.VideoCapture(1)
    # cam2.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    # cam2.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    #
    # time.sleep(1.5)
    #
    # r, i = cam2.read()
    # cam2.release()
    #
    # cv2.imshow("Nice", i)
    # cv2.destroyWindow("Nice")
    # cv2.imwrite(PATH_IMG2, i)


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
    B, L, D = process_cam1()
    return "".join(U) + "".join(R) + "".join(F) + "".join(B) + "".join(L) + "".join(D)
