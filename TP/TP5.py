import cv2 as cv 
img = cv.imread("fruit3.jpg")
# image = cv.imshow("Image",img)
image=img.copy()

def darkness():
    # darkness =image.copy(img)
    modify_value= 100
    for x in range(len(image)):
        for y in range(len(image[x])):
            #Operation 
            new_B = image[x,y,2] - modify_value  #Index 2 represents the Blue channel.
            new_G = image[x,y,1] - modify_value  #Index 1 represents the Green channel.
            new_R = image[x,y,0] - modify_value  #Index 0 represents the Red channel.

            # check condition of the intensity which is smaller than 0
            if new_B < 0:
                new_B = 0
            if new_G < 0:
                new_G=0
            if new_R <0:
                new_R=0
            #Add new intensity which has modified value
            darkness[x,y] = [new_B,new_G,new_R]
    cv.imshow("Darkness Image",darkness)
    
def brightness():
    # brightness= img.copy(img)
    modify_value= 100

    #loop for  iterate over each pixel in the image.
    for x in range(len(image)):
        for y in range(len(image[x])):
            #Operation 
            new_B = modify_value + image[x,y,2]
            new_G = modify_value + image[x,y,1]
            new_R = modify_value + image[x,y,0]

            # check condition of the intensity which is bigger than 255
            if new_B > 255:
                new_B = 255
            if new_G > 255:
                new_G = 255
            if new_R > 255:
                new_R = 255
            #Add new intensity which has modified value
            brightness[x,y] = [new_B,new_G,new_R]
    cv.imshow("Brightness Image",brightness)
    
# image
darkness()
brightness()
cv.waitKey(0)
