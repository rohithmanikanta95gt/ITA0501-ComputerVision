import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the image in grayscale (erosion is a morphological operation)
image_path = "your_image.jpg" 
img_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if img_gray is None:
    print("Error: Could not load the image. Check the file name.")
else:
    # 2. Define the structuring element (kernel)
    # A 5x5 matrix of ones. Bigger numbers mean stronger erosion.
    kernel = np.ones((5, 5), np.uint8)
    
    # 3. Apply the Erode function
    # iterations=1 means the erosion process happens once
    img_eroded = cv2.erode(img_gray, kernel, iterations=1)
    
    # 4. Display both images side-by-side inline
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    # Original Grayscale
    axes[0].imshow(img_gray, cmap='gray')
    axes[0].set_title("Original Grayscale")
    axes[0].axis('off')
    
    # Eroded Result
    axes[1].imshow(img_eroded, cmap='gray')
    axes[1].set_title("Eroded Image")
    axes[1].axis('off')
    
    plt.show()
