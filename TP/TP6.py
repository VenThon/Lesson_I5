from math import floor
#histogram equalized color image

import cv2
img = cv2.imread('./glass.jpg')
copy_img=img.copy()
height,width,kernel=copy_img.shape

histoR=(256)*[0]
histoG=(256)*[0]
histoB=(256)*[0]

#lookup table
LUTR=(256)*[0]
LUTG=(256)*[0]
LUTB=(256)*[0]
for i in range(height):
    for j in range(width):
        r,g,b = img[i,j]
        histoR[r]+=1
        histoG[g]+=1
        histoB[b]+=1
#build histogram original
for i in range(256):
    #change if i ==0 so we give histogram equal to its index at 0   
    if i ==0:
        histoB[i]=histoB[0]
        histoG[i]=histoG[0]
        histoR[i]=histoR[0]
    else:
        #check the rest calculate like take current index + index-1
        histoB[i]=histoB[i]+histoB[i-1]
        histoG[i]=histoG[i]+histoG[i-1]
        histoR[i]=histoR[i]+histoR[i-1]

#transform histogram
for i in range(256):
    LUTB[i] = (float(histoB[i])/float(width*height))*255
    LUTG[i] = (float(histoG[i])/float(width*height))*255
    LUTR[i] = (float(histoR[i])/float(width*height))*255

    #loop row image
for i in range(height):
   
   #loop column hight
   for j in range(width):
        # Write your code here

        #look up orininal image
        b, g, r = img[i,j]
        #New intensity value of channel muy muy R G B
        copy_img[i,j,0]= LUTB[r]
        copy_img[i,j,1]= LUTB[g]
        copy_img[i,j,2]= LUTB[b]

cv2.imshow('Histogram',copy_img)
cv2.imshow("Original",img)
cv2.waitKey()