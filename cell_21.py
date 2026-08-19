import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the original color image
image_path = "your_image.jpg" 
img = cv2.imread(image_path)

if img is None:
    print("Error: Could not load the image. Check the file name.")
else:
    # Convert to grayscale as morphological operations require a single channel
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 2. Define a structural element (Kernel)
    kernel = np.ones((9, 9), np.uint8)
    
    # 3. Apply the Black Hat operation
    img_blackhat = cv2.morphologyEx(img_gray, cv2.MORPH_BLACKHAT, kernel)
    
    # 4. Display both original grayscale and Black Hat output side-by-side
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))
    
    # Subplot 0: Original View
    axes[0].imshow(img_gray, cmap='gray')
    axes[0].set_title("Original Grayscale Image")
    axes[0].axis('off')
    
    # Subplot 1: Black Hat View
    axes[1].imshow(img_blackhat, cmap='gray')
    axes[1].set_title("Black Hat (Dark Elements Extracted)")
    axes[1].axis('off')
    
    plt.tight_layout()
    plt.show()
