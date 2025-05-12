# utils.py
import cv2                                                              # Import OpenCV library for image processing



# Function to load image from path and convert to RGB format
def load_image(image_path):
    img = cv2.imread(image_path)                                        # Read the image in BGR format (default in OpenCV)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)                      # Convert the image from BGR to RGB
    return img_rgb                                                      # Return the RGB image
