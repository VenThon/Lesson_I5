#Import the OpenCV library and NumPy:
import cv2 as cv
import numpy as np

#Read the original image 
img =cv.imread("facetree.jpg")
# imgMirror = cv.imread("facetree.jpg")

#Create a deep copy of the original image using NumPy's
copyimage = np.copy(img)

#loop function 
def mirrorLeft(copyimage): 
    for w in range(len(img)):
        #Len is  length of an object.
        for h in range(len(img[w])): 
            #left image to right image use h-1
            copyimage[w,h] = img[w,len(img[w,h])-h-1]
    return copyimage

def mirrorTopRight(copyimage): 
    for w in range(len(img)):
        for h in range(len(img[w])): 
            #left top right to bottom lef use w-1
            copyimage[w,h] = img[len(img[w,h])-w-1,h]
    return copyimage

def mirrorTopLeft(copyimage):  
    for w in range(len(img)):
        for h in range(len(img[w])): 
            #top left to the bottom right use h -1 
            copyimage[w,h] = img[len(img[w,h])-w-1,len(img[w,h])-h-1]
    return copyimage

cv.imshow("image",img)       
cv.imshow("mirror left", mirrorLeft(copyimage))
cv.imshow("mirror top right", mirrorTopRight(copyimage))
cv.imshow("mirror top left",mirrorTopLeft(copyimage))
cv.waitKey(0)

# used wait for a key event  after displaying the images.