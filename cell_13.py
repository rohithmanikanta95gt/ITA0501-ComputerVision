import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the original color image
image_path = "your_image.jpg" 
img = cv2.imread(image_path)

if img is None:
    print("Error: Could not load the image. Check the file name.")
else:
    # Convert to grayscale as Sobel works on single-channel intensity values
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 2. Apply Sobel Filter in X-direction (detects vertical edges)
    # cv2.CV_64F preserves negative gradients (black-to-white transitions)
    sobelx = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=3)
    
    # 3. Apply Sobel Filter in Y-direction (detects horizontal edges)
    sobely = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=3)
    
    # 4. Take absolute values and convert back to 8-bit unsigned integers
    sobelx_abs = cv2.convertScaleAbs(sobelx)
    sobely_abs = cv2.convertScaleAbs(sobely)
    
    # 5. Combine the X and Y gradient results together
    sobel_combined = cv2.addWeighted(sobelx_abs, 0.5, sobely_abs, 0.5, 0)
    
    # 6. Display all results in a 1x4 subplot grid for detailed comparison
    fig, axes = plt.subplots(1, 4, figsize=(22, 5))
    
    # Display Original Grayscale
    axes[0].imshow(img_gray, cmap='gray')
    axes[0].set_title("Original Grayscale")
    axes[0].axis('off')
    
    # Display Sobel X
    axes[1].imshow(sobelx_abs, cmap='gray')
    axes[1].set_title("Sobel X (Vertical Edges)")
    axes[1].axis('off')
    
    # Display Sobel Y
    axes[2].imshow(sobely_abs, cmap='gray')
    axes[2].set_title("Sobel Y (Horizontal Edges)")
    axes[2].axis('off')
    
    # Display Combined Sobel
    axes[3].imshow(sobel_combined, cmap='gray')
    axes[3].set_title("Sobel Combined")
    axes[3].axis('off')
    
    plt.tight_layout()
    plt.show()
