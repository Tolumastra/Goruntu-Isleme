import cv2
import numpy as np
import matplotlib.pyplot as plt

# Örnek bir gri seviye görüntü oluşturun (örneğin, 0 ile 255 arasında rastgele piksel değerleri)
image = cv2.imread("dragon.jpg",0)

# Görüntüyü histogramı hesapla
histogram = np.zeros(256, dtype=int)

# Görüntüdeki her pikseli dolaşarak histogramı hesapla
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        pixel_value = image[i, j]
        histogram[pixel_value] += 1

# Histogramı görselleştirin
plt.bar(range(256), histogram, width=1, color='gray')
plt.title("Gri Seviye Görüntü Histogramı")
plt.xlabel("Piksel Değeri")
plt.ylabel("Piksel Sayısı")
plt.show()
