
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pygame
import time
import pygame.camera
from PIL import Image
import cv2
PATH_IMG1 = "./cam1.jpg"


pygame.camera.init()
pygame.camera.list_cameras()

# cam1 = pygame.camera.Camera("/dev/video0", (640, 480))
cam1 = cv2.VideoCapture(0)
cam1.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam1.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
time.sleep(3)
result, image = cam1.read()
cam1.release()

print(result)

if result:
    cv2.imshow("Nice", image)
    cv2.imwrite(PATH_IMG1, image)
    cv2.waitKey(0)
    cv2.destroyWindow("Nice")


image = Image.open(PATH_IMG1)
plt.imshow(image)
plt.show()
