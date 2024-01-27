#import OpenCV library
import cv2
#Read image orinal image
image_path=cv2.imread('./fruit1.jpg')
#copy of the original image to modifying 
image_copy=image_path.copy()
#Determine height, width, and number of color channels( R, G, B) of image
height, width, channel = image_copy.shape

#ceate function loop 
def convert_to_grayscale(image_copy):
    #loop on height width determind value pixel
    for i in range(height):
        for j in range(width):
            #Get the RGB value of the pixel
            r,g,b = image_copy[i,j]
            #Calculate the value RGB
            intensity=0.587*r +0.299*g +0.114*b
            #Call value RGB to grayscal to use
            image_copy[i,j]=(intensity, intensity, intensity)
    return image_copy

grayscal_image = convert_to_grayscale(image_copy)

#Display 
cv2.imshow("Original", image_path)
cv2.imshow("grayscale", grayscal_image)
cv2.waitKey()