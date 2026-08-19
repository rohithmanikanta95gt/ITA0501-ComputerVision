import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the original color image
image_path = "your_image.jpg" 
img = cv2.imread(image_path)

if img is None:
    print("Error: Could not load the image. Check the file name.")
else:
    # Convert to grayscale as morphological operations require a single-channel image
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 2. Define the structural matrix element (Kernel)
    # A 5x5 square matrix filled with ones. Larger sizes cause heavier erosion.
    kernel = np.ones((5, 5), np.uint8)
    
    # 3. Apply the Erosion function
    # iterations=1 means the erosion filter process runs through the loop once
    img_eroded = cv2.erode(img_gray, kernel, iterations=1)
    
    # 4. Display both original grayscale and eroded output side-by-side
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))
    
    # FIX: Use indexing [0] for the first subplot layout window
    axes[0].imshow(img_gray, cmap='gray')
    axes[0].set_title("Original Grayscale Image")
    axes[0].axis('off')
    
    # FIX: Use indexing [1] for the second subplot layout window
    axes[1].imshow(img_eroded, cmap='gray')
    axes[1].set_title("Eroded Image (Shrunk White Elements)")
    axes[1].axis('off')
    
    plt.tight_layout()
    plt.show()
