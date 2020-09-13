import numpy as np
import matplotlib.pyplot as plt
img=plt.imread('roi.jpg')
roi=img[880:1040, 1030:1190,:]
image=img.copy()
final_place=image[836:996, 220:380,:]
final_place[:,:,:]=roi[:,:,:]
plt.imshow(img)
plt.show()
plt.imshow(image)
plt.show()
