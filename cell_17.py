import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the original color image
image_path = "your_image.jpg" 
img = cv2.imread(image_path)

if img is None:
    print("Error: Could not load the image. Check the file name.")
else:
    # Convert to grayscale as morphological operations work on single-channel intensity
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 2. Define the structural matrix element (Kernel)
    # A 5x5 square matrix filled with ones. Larger sizes create a thicker effect.
    kernel = np.ones((5, 5), np.uint8)
    
    # 3. Apply the Dilation function
    # iterations=1 means the dilation filter loop runs once
    img_dilated = cv2.dilate(img_gray, kernel, iterations=1)
    
    # 4. Display both original grayscale and dilated output side-by-side
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))
    
    # Subplot 0: Original Grayscale
    axes[0].imshow(img_gray, cmap='gray')
    axes[0].set_title("Original Grayscale Image")
    axes[0].axis('off')
    
    # Subplot 1: Dilated Result
    axes[1].imshow(img_dilated, cmap='gray')
    axes[1].set_title("Dilated Image (Expanded White Elements)")
    axes[1].axis('off')
    
    plt.tight_layout()
    plt.show()
