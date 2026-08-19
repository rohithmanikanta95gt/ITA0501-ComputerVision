import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the image
image_path = "your_image.jpg" 
img = cv2.imread(image_path)

if img is None:
    print("Error: Could not load the image. Check the file name.")
else:
    # Make a copy to draw on, and convert to grayscale (required for Harris)
    img_result = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Convert data type to float32 (required by cornerHarris)
    img_gray = np.float32(img_gray)
    
    # 2. Apply Harris Corner Detection
    dst = cv2.cornerHarris(img_gray, blockSize=2, ksize=3, k=0.04)
    
    # Dilate the result just to make the detected corner points look larger/clearer
    dst = cv2.dilate(dst, None)
    
    # FIX: Set the replacement color channel array values to Pure Red [255, 0, 0]
    img_result[dst > 0.01 * dst.max()] = [255, 0, 0]
    
    # 4. Display both images side-by-side
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))
    
    # Original Input
    img_original_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    axes[0].imshow(img_original_rgb)
    axes[0].set_title("Original Image")
    axes[0].axis('off')
    
    # Output with Red Dots on Corners
    axes[1].imshow(img_result)
    axes[1].set_title("Harris Corners Detected (Red)")
    axes[1].axis('off')
    
    plt.tight_layout()
    plt.show()
