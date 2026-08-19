import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the original color image
image_path = "your_image.jpg" 
img = cv2.imread(image_path)

if img is None:
    print("Error: Could not load the image. Check the file name.")
else:
    # Convert to grayscale as morphological operations process single-channel matrices
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 2. Define the structural matrix element (Kernel)
    # A 5x5 square matrix filled with ones. Adjust size based on your image noise scale.
    kernel = np.ones((5, 5), np.uint8)
    
    # 3. Apply the Opening Morphological operation
    # cv2.MORPH_OPEN handles the erosion -> dilation pipeline seamlessly in one line
    img_opened = cv2.morphologyEx(img_gray, cv2.MORPH_OPEN, kernel)
    
    # 4. Display both original grayscale and opened output side-by-side
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))
    
    # Subplot 0: Original View
    axes[0].imshow(img_gray, cmap='gray')
    axes[0].set_title("Original Grayscale Image")
    axes[0].axis('off')
    
    # Subplot 1: Opened View
    axes[1].imshow(img_opened, cmap='gray')
    axes[1].set_title("Opened Image (Background Noise Removed)")
    axes[1].axis('off')
    
    plt.tight_layout()
    plt.show()
