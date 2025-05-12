import cv2                                                        # Import OpenCV library
import numpy as np                                                # Import NumPy library
from skimage import color                                         # Import color module from scikit-image
from skimage.filters import sobel                                 # Import Sobel edge detection filter from scikit-image




# Brightness function
def increase_brightness(img, value=30):# Function to increase image brightness
    matrix = np.ones(img.shape, dtype="uint8") * value            # Create a matrix of ones and multiply it by the brightness value
    bright_img = cv2.add(img, matrix)                             # Add the matrix to the image to increase brightness
    return bright_img                                             # Return the brightened image




# Contrast function
def increase_contrast(img, factor=1.2):# Function to increase image contrast
    img = np.clip(img * factor, 0, 255).astype("uint8")           # Apply contrast factor and clip values to be in the range [0, 255]
    return img                                                    # Return the contrast-enhanced image




# Denoising function
def remove_noise(img):# Function to remove noise from the image
    return cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)     # Apply Non-Local Means Denoising to the colored image



# Histogram Equalization function
def equalize_histogram(img):# Function for histogram equalization
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)                         # Convert the image to grayscale
    eq = cv2.equalizeHist(gray)                                          # Apply histogram equalization to the grayscale image
    return cv2.cvtColor(eq, cv2.COLOR_GRAY2RGB)                          # Convert the equalized grayscale image back to RGB




# Morphological Operations function
def morphological_operations(img):# Function to apply morphological operations
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)                           # Convert the image to grayscale
    kernel = np.ones((5, 5), np.uint8)                                     # Create a kernel for morphological operation
    morphed = cv2.dilate(gray, kernel, iterations=1)                       # Apply dilation (morphological operation)
    return cv2.cvtColor(morphed, cv2.COLOR_GRAY2RGB)                       # Convert the morphed grayscale image back to RGB




# Sharpness function
def sharpen_image(img): # Function to sharpen the image
    kernel = np.array([[-1, -1, -1],      # Sharpening kernel
                       [-1,  9, -1],
                       [-1, -1, -1]])
    return cv2.filter2D(img, -1, kernel)  # Apply the sharpening kernel to the image




# Sobel Edge Detection function
def sobel_edge_enhancement(img):# Function for Sobel edge detection enhancement
    gray = color.rgb2gray(img)                                             # Convert the image to grayscale using skimage
    edges = sobel(gray)                                                    # Apply Sobel edge detection
    edges_uint8 = (edges * 255).astype("uint8")                            # Convert the edge map to uint8 format
    return cv2.cvtColor(edges_uint8, cv2.COLOR_GRAY2RGB)                   # Convert the edge image back to RGB




# Gamma Correction function
def gamma_correction(img, gamma=4): # Function for gamma correction
    invGamma = 1.0 / gamma                                                                   # Calculate the inverse gamma value
    table = (np.array([(i / 255.0) ** invGamma * 255 for i in range(256)])).astype("uint8")  # Create a lookup table for gamma correction
    return cv2.LUT(img, table)                                                               # Apply the lookup table to the image




# Increase Saturation function
def enhance_saturation(img, scale=5):# Function to increase the saturation of the image
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)                                               # Convert the image to HSV color space
    hsv = np.array(hsv, dtype=np.float32)                                                    # Convert to float32 for processing
    hsv[..., 1] *= scale                                                                     # Increase the saturation channel (second channel in HSV)
    hsv[..., 1] = np.clip(hsv[..., 1], 0, 255)                                               # Clip the values to be within the valid range
    hsv = np.array(hsv, dtype=np.uint8)                                                      # Convert back to uint8
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)                                              # Convert the image back to RGB color space




# CLAHE (Contrast Limited Adaptive Histogram Equalization) function
def apply_clahe(img):# Function to apply CLAHE to enhance image contrast
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)                                             # Convert the image to grayscale
    clahe = cv2.createCLAHE(clipLimit=5, tileGridSize=(8, 8))                                # Create a CLAHE object
    clahe_img = clahe.apply(gray)                                                            # Apply CLAHE to the grayscale image
    return cv2.cvtColor(clahe_img, cv2.COLOR_GRAY2RGB)                                       # Convert the CLAHE image back to RGB




# Gaussian Blur function
def gaussian_blur(img, kernel_size=(5, 5), sigma=1.5): # Function to apply Gaussian blur to the image
    blurred_img = cv2.GaussianBlur(img, kernel_size, sigma)                                             # Apply Gaussian blur
    return blurred_img                                                                                  # Return the blurred image

# Invert Colors function
def invert_colors(img): # Function to invert the colors of the image
    inverted_img = cv2.bitwise_not(img)                                                # Invert the image using bitwise NOT operation
    return inverted_img                                                                # Return the inverted image




# Adjust Color Balance function
def adjust_color_balance(img, red_factor=1.0, green_factor=2.5, blue_factor=1.0):# Function to adjust color balance
    img[..., 0] = np.clip(img[..., 0] * blue_factor, 0, 255)                                         # Adjust the blue channel
    img[..., 1] = np.clip(img[..., 1] * green_factor, 0, 255)                                        # Adjust the green channel
    img[..., 2] = np.clip(img[..., 2] * red_factor, 0, 255)                                          # Adjust the red channel
    return img  # Return the color-balanced image




# Apply Thermal Color Map function
def apply_color_map(img):# Function to apply a thermal color map to the image
    thermal_img = cv2.applyColorMap(img, cv2.COLORMAP_JET)                                        # Apply the JET colormap to the image
    return thermal_img                                                                            # Return the thermal map image
 