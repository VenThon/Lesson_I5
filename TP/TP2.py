#import OpenCV library
import cv2
#Read image orinal image
image_orinal=cv2.imread('./fruit4.jpg')
#copy of the original image to modifying 
image_inverse=image_orinal.copy()

#Determine height, width, and number of color channels( R, G, B) of image
height, width, channel = image_inverse.shape

#ceate function loop 
def inverse_color(image_inverse):
    for i in range(height):
        for j in range(width):
            #Get the RGB value of the pixel
            r,g,b= image_inverse[i,j]
            # So the hight value of RGB is 255 and Value of color black = 0
            # We need Value 255-0, to display image is black
            intensityR=255-r
            intensityG=255-g
            intensityB=255-b

            # Update the pixel with the inverted color
            image_inverse[i,j]=(intensityR,intensityG, intensityB)
    return image_inverse

image_inverse_color=inverse_color(image_inverse)
# Display 
cv2.imshow("Original", image_orinal)
cv2.imshow("Inverse", image_inverse_color)
cv2.waitKey()