import cv2
import numpy as np

#Ucitavanje slike
image=cv2.imread('polo.jpg')

#Pretvorba iz BGR u RGB
image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

#Definisanje gornjih i donjih ivica za plavu boju u BGR
lower_blue=np.array([0,0,100],dtype=np.uint8)
upper_blue=np.array([100,100,255],dtype=np.uint8)

#Napravi masku gdje su plavi pikseli postavljeni na 255(bijelo),a neplavi pikseli postavljeni na 0(crno)
mask_blue=cv2.inRange(image_rgb,lower_blue,upper_blue)

#Invertuj masku tako da su plavi pikseli postavljeni na 0(crno),a neplavi pikseli postavljeni na 255(bijelo)
mask_not_blue=cv2.bitwise_not(mask_blue)

#Napravi bijelu sliku
white_image=np.ones_like(image)*255

#Zamjeni plave dijelove originalne slike bijelom bojom
result=cv2.bitwise_and(image,image,mask=mask_not_blue)+cv2.bitwise_and(white_image,white_image,mask=mask_blue)

#Prikaz rezultata
cv2.imwrite('result_image.jpg',result)
