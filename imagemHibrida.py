import numpy as np
import cv2
import matplotlib.pyplot as plt
import sys
from math import sqrt

def distancia(pt1, pt2):
    return sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)

def gaussianFilter(d0, shape, high_pass = False):
    base = np.zeros(shape[:2])
    rows, cols = shape[:2]
    center_row, center_col = rows / 2, cols / 2
    
    for i in range(rows):
        for j in range(cols):
            base[i, j] = np.exp(-distancia((i, j), (center_row, center_col))**2 / d0**2)
            
    if high_pass == True:
        return 1-base
    
    return base

def hybridImg(img1, img2, d0_low=20, d0_high=20):
    # aplicando fftshift nas ffts das imagens
    fft1 = np.fft.fftshift(np.fft.fft2(np.float32(img1)))
    fft2 = np.fft.fftshift(np.fft.fft2(np.float32(img2)))
    
    #passa-baixa e passa-alta 
    lp = fft1 * gaussianFilter(d0_low, img1.shape, high_pass = False)
    hp = fft2 * gaussianFilter(d0_high, img2.shape, high_pass = True)
    
    #voltando para o domínio da imagem
    inv_lp = np.fft.ifft2(np.fft.ifftshift(lp))
    inv_hp = np.fft.ifft2(np.fft.ifftshift(hp))
    
    hybrid = np.real(inv_lp + inv_hp)
    hybrid = cv2.normalize(hybrid, None, 0, 255, cv2.NORM_MINMAX)
    
    return np.uint8(hybrid)

img1 = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(sys.argv[2], cv2.IMREAD_GRAYSCALE)

img1 = cv2.resize(img1, (512, 512))
img2 = cv2.resize(img2, (512, 512))

imgHibrida = hybridImg(img1, img2, 35, 20)

plt.subplot(1, 3, 1)
plt.imshow(img1, cmap='gray')
plt.title("Passa-baixa")
plt.subplot(1, 3, 2)
plt.imshow(img2, cmap='gray')
plt.title("Passa-alta")
plt.subplot(1, 3, 3)
plt.imshow(imgHibrida, cmap='gray')
plt.title("Imagem Híbrida")
plt.show()
