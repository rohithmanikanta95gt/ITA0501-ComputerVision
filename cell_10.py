import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the original color image
image_path = "your_image.jpg" 
img = cv2.imread(image_path)

if img is None:
    print("Error: Could not load the image. Check the file name.")
else:
    # Convert from BGR to RGB for Jupyter display
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Get image dimensions (height and width)
    rows, cols, ch = img_rgb.shape
    
    # 2. Define 3 coordinates on the original image
    # (Top-left, top-right, and bottom-left reference corners)
    points_original = np.float32([[50, 50], [cols - 50, 50], [50, rows - 50]])
    
    # 3. Define where those 3 coordinates should move to in the output image
    # (Shifting the corners to create a skewed, perspective-like affine effect)
    points_target = np.float32([[10, 100], [cols - 80, 50], [100, rows - 10]])
    
    # 4. Generate the 2x3 Affine Transformation Matrix
    matrix = cv2.getAffineTransform(points_original, points_target)
    
    # 5. Apply the transformation matrix to warp the image
    # (cols, rows) sets the size of the final output canvas
    img_affine = cv2.warpAffine(img_rgb, matrix, (cols, rows))
    
    # 6. Display both images side-by-side
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))
    
    # Original Image Panel
    axes[0].imshow(img_rgb)
    axes[0].set_title("Original Image")
    axes[0].axis('off')
    
    # Affine Transformed Panel
    axes[1].imshow(img_affine)
    axes[1].set_title("Affine Transformed Image")
    axes[1].axis('off')
    
    plt.tight_layout()
    plt.show()
