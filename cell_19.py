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
    # A 5x5 square matrix filled with ones. Adjust size based on the size of the gaps.
    kernel = np.ones((5, 5), np.uint8)
    
    # 3. Apply the Closing Morphological operation
    # cv2.MORPH_CLOSE handles the dilation -> erosion pipeline seamlessly in one line
    img_closed = cv2.morphologyEx(img_gray, cv2.MORPH_CLOSE, kernel)
    
    # 4. Display both original grayscale and closed output side-by-side
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))
    
    # Subplot 0: Original View
    axes[0].imshow(img_gray, cmap='gray')
    axes[0].set_title("Original Grayscale Image")
    axes[0].axis('off')
    
    # Subplot 1: Closed View
    axes[1].imshow(img_closed, cmap='gray')
    axes[1].set_title("Closed Image (Internal Gaps/Holes Filled)")
    axes[1].axis('off')
    
    plt.tight_layout()
    plt.show()
