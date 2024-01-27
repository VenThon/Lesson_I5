# Function to store 2D image data as a 2D array
def store_image_data(image):
    rows = len(image)
    cols = len(image[0])

    # Create a 3D array to store the pixel values
    data = [[[0, 0, 0] for _ in range(cols)] for _ in range(rows)]

    # Iterate over each pixel in the image
    for i in range(rows):
        for j in range(cols):
            # Store the RGB values of the pixel in the array
            data[i][j] = image[i][j]

    return data