📸 Image Enhancement Project – Python
This project is a simple and interactive tool for enhancing images using common techniques in digital image processing. It's built with Python and OpenCV, and allows users to apply various enhancements to an image through a terminal-based interface.

🎯 Objective
To allow users to improve the visual quality of their images using different enhancement methods such as brightness, contrast, denoising, and more — with instant visual feedback by comparing the original and enhanced versions side by side.

🛠️ How It Works
The user runs the program.

They are prompted to select an image from their system.

They are then presented with a list of 14 enhancement options.

After selecting an option, the enhancement is applied to the image.

The program displays the original image and the enhanced image for comparison.

Optionally, the user can choose to save the result.

✨ Available Enhancement Options
Below are the enhancements available in the project, each serving a unique purpose:

Brightness – Increases the overall lightness of the image, making dark areas more visible.

Contrast – Enhances the difference between light and dark areas, making features more distinguishable.

Denoising – Reduces visual noise or grain from the image, often caused by poor lighting or compression.

Histogram Equalization – Spreads out the most frequent intensity values to improve global contrast in grayscale images.

Morphological Operations – Applies basic image morphology like dilation and erosion, useful for removing small noise or separating connected objects.

Sharpness – Enhances the edges and fine details in the image, making it appear more focused and crisp.

Sobel Edge Enhancement – Detects edges using the Sobel filter and highlights the transitions between different regions.

Gamma Correction – Adjusts the brightness of the image in a nonlinear way, useful for correcting lighting conditions.

Enhance Saturation – Makes the colors in the image more vivid and vibrant without changing brightness.

CLAHE (Contrast Limited Adaptive Histogram Equalization) – Improves contrast locally while avoiding over-amplification of noise; ideal for medical or low-light images.

Gaussian Blur – Smoothens the image by averaging pixel values, reducing detail and noise (often used as a preprocessing step).

Invert Colors – Flips all color values, creating a negative of the image (useful in medical or creative contexts).

Adjust Color Balance – Alters the balance of RGB channels to fix color tone or create a different visual mood.

Apply Color Map – Applies a predefined colormap to grayscale images, making them more visually informative (e.g., heatmaps).

🖼️ Output Example
After applying any enhancement, the tool will display:

Left: Original image

Right: Enhanced version
This allows quick visual comparison to evaluate the impact of the selected technique.


🚀 How to Run
Clone the repository.

Place your test images in the specified folder or adjust the image path in the code.

Run the main Python script.

Follow the prompts in the terminal to apply an enhancement and view results.
