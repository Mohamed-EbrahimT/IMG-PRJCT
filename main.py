import cv2                                                                                    
import matplotlib.pyplot as plt                                                        # Import matplotlib for image display



# Import enhancement functions from custom enhancement module
from enhancement import (
    increase_brightness,
    increase_contrast,
    remove_noise,
    equalize_histogram,
    morphological_operations,
    sharpen_image,
    sobel_edge_enhancement , 
    gamma_correction ,
    enhance_saturation , 
    apply_clahe ,
    gaussian_blur , 
    invert_colors , 
    adjust_color_balance , 
    apply_color_map
)



# Load the image using OpenCV
img = cv2.imread("E:/ImageEnhancementProject/Dataset/test/cat_56.jpg")                # Read image in BGR format
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)                                        # Convert image to RGB format for correct display





# Display enhancement options to the user
print("Choose the enhancement operation to apply:")
print("1. Brightness")
print("2. Contrast")
print("3. Denoising")
print("4. Histogram Equalization")
print("5. Morphological Operations")
print("6. Sharpness")
print("7. Sobel Edge Enhancement")
print("8. Gamma Correction")
print("9. Enhance Saturation")
print("10. CLAHE")
print("11. Gaussian Blur")
print("12. Invert Colors")
print("13. Adjust Color Balance")
print("14. Apply Color Map")



choice = input("Enter the number of the operation: ")                               # Take the input (option) from user

operation_name = ""                                                                #Initialize the operation name to use it in if condition and in later display


# Apply the selected enhancement operation based on user input
if choice == "1":
    result = increase_brightness(img_rgb)
    operation_name = "Brightness"
elif choice == "2":
    result = increase_contrast(img_rgb)
    operation_name = "Contrast"
elif choice == "3":
    result = remove_noise(img_rgb)
    operation_name = "Denoising"
elif choice == "4":
    result = equalize_histogram(img_rgb)
    operation_name = "Histogram Equalization"
elif choice == "5":
    result = morphological_operations(img_rgb)
    operation_name = "Morphological Operations"
elif choice == "6":
    result = sharpen_image(img_rgb)
    operation_name = "Sharpness"
elif choice == "7":
    result = sobel_edge_enhancement(img_rgb)
    operation_name = "Sobel Edge Enhancement"
elif choice == "8":
    result = gamma_correction(img_rgb)
    operation_name = "Gamma Correction"
elif choice == "9":
    result = enhance_saturation(img_rgb)
    operation_name = "Enhance Saturation"
elif choice == "10":
    result = apply_clahe(img_rgb)
    operation_name = "CLAHE"
elif choice == "11":
    result = gaussian_blur(img_rgb)
    operation_name = "Gaussian Blur"
elif choice == "12":
    result = invert_colors(img_rgb)
    operation_name = "Invert Colors"
elif choice == "13":
    result = adjust_color_balance(img_rgb)
    operation_name = "Adjust Color Balance"
elif choice == "14":
    result = apply_color_map(img_rgb)
    operation_name = "Apply Color Map"

else:
    print("Invalid choice.")                                                  # Handle invalid input
    exit()                                                                    # Exit the program if input is invalid




# Display original and enhanced image side by side
plt.figure(figsize=(10, 5))                                                  #create an interface (figsize) to display images with specific size
plt.subplot(1, 2, 1)                                                         # First subplot (part) for original image
plt.imshow(img_rgb)                                                          # Show original image
plt.title("Original Image")                                                  # Set title for original image
plt.axis("off")                                                              # Hide axis


plt.subplot(1, 2, 2)                                                         # Second subplot (part) for enhanced image
plt.imshow(result)                                                           # Show enhanced image
plt.title(f"After {operation_name}")                                        # Set title with enhancement name
plt.axis("off")

plt.tight_layout()                        
plt.show()                                                                  # Display the interface with images(figure)




# Ask user if they want to save the result
save_choice = input("Do you want to save the result? (y/n): ")
if save_choice.lower() == 'y':
    save_path = input("Enter the path to save the image (e.g., E:/path_to_save/result.jpg): ")        # Get save path
    result_bgr = cv2.cvtColor(result, cv2.COLOR_RGB2BGR)                                              # Convert back to BGR before saving
    cv2.imwrite(save_path, result_bgr)                                                               # Save the image to the specified path
    print(f"Image saved at {save_path}")                                                             # Confirm save location



