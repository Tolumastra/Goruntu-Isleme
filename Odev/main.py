import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("dragon.jpg",0)

histogram = np.zeros(256, dtype=int)

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        pixel_value = image[i, j]
        histogram[pixel_value] += 1

plt.bar(range(256), histogram, width=1, color='gray')
plt.title("Gri Seviye Görüntü Histogramı")
plt.xlabel("Piksel Değeri")
plt.ylabel("Piksel Sayısı")
plt.show()
