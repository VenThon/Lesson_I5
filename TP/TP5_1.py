import cv2 as cv

def apply_darkness(image, modify_value=100):
    height, width, channels = image.shape
    modified_image = image.copy()
    
    for y in range(height):
        for x in range(width):
            # Extracting the intensity values of the pixel
            intensity = image[y, x]
            
            # Calculating the modified intensity using the darkness formula
            modified_intensity = (intensity[0] - modify_value, intensity[1] - modify_value, intensity[2] - modify_value)
            
            # Checking if the modified intensity is less than 0 and setting it to 0 if true
            modified_intensity = tuple(max(value, 0) for value in modified_intensity)
            
            # Assigning the modified intensity to the pixel
            modified_image[y, x] = modified_intensity
    
    return modified_image

def apply_brightness(image, modify_value=100):
    height, width, channels = image.shape
    modified_image = image.copy()
    
    for y in range(height):
        for x in range(width):
            # Extracting the intensity values of the pixel
            intensity = image[y, x]
            
            # Calculating the modified intensity using the brightness formula
            modified_intensity = (intensity[0] + modify_value, intensity[1] + modify_value, intensity[2] + modify_value)
            
            # Checking if the modified intensity is greater than 255 and setting it to 255 if true
            modified_intensity = tuple(min(value, 255) for value in modified_intensity)
            
            # Assigning the modified intensity to the pixel
            modified_image[y, x] = modified_intensity
    
    return modified_image

# Load the image
image = cv.imread("fruit3.jpg")

# Apply darkness with modify_value = 100
darkness_image = apply_darkness(image, modify_value=100)

# Apply brightness with modify_value = 100
brightness_image = apply_brightness(image, modify_value=100)

# Display the original image, darkness image, and brightness image
cv.imshow("Original Image", image)
cv.imshow("Darkness Image", darkness_image)
cv.imshow("Brightness Image", brightness_image)

cv.waitKey(0)
cv.destroyAllWindows()