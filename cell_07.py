import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the image in grayscale
image_path = "your_image.jpg" 
img_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if img_gray is None:
    print("Error: Could not load the image. Check the file name.")
else:
    # 2. Define the structuring element (kernel)
    kernel = np.ones((5, 5), np.uint8)
    
    # 3. Apply the Dilate function
    img_dilated = cv2.dilate(img_gray, kernel, iterations=1)
    
    # 4. Display both images side-by-side inline
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    # FIX: Use axes[0] for the first image
    axes[0].imshow(img_gray, cmap='gray')
    axes[0].set_title("Original Grayscale")
    axes[0].axis('off')
    
    # FIX: Use axes[1] for the second image
    axes[1].imshow(img_dilated, cmap='gray')
    axes[1].set_title("Dilated Image")
    axes[1].axis('off')
    
    plt.show()
