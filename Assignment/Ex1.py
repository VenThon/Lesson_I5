# Function to store 2D image data as a 2D array
def store_image_data(image):
    rows = len(image)
    cols = len(image[0])

    # Create a 2D array to store the pixel values
    data = [[0] * cols for _ in range(rows)]

    # Iterate over each pixel in the image
    for i in range(rows):
        for j in range(cols):
            # Store the pixel value in the array
            data[i][j] = image[i][j]

    return data