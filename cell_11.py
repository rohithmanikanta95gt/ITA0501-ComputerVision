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
    height, width, ch = img_rgb.shape
    
    # FIX: Defined all 4 corner source points accurately
    pts_original = np.float32([[0, 0], [width - 1, 0], [0, height - 1], [width - 1, height - 1]])
    
    # FIX: Defined destination mapping points to squeeze the top inwards (creates a 3D road effect)
    pts_target = np.float32([[int(width * 0.15), int(height * 0.2)], 
                             [int(width * 0.85), int(height * 0.2)], 
                             [0, height - 1], 
                             [width - 1, height - 1]])
    
    # 4. Generate the 3x3 Perspective Transformation Matrix
    matrix = cv2.getPerspectiveTransform(pts_original, pts_target)
    
    # 5. Apply the perspective transformation matrix to warp the image
    img_perspective = cv2.warpPerspective(img_rgb, matrix, (width, height))
    
    # 6. Display both images side-by-side
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))
    
    axes[0].imshow(img_rgb)
    axes[0].set_title("Original Image")
    axes[0].axis('off')
    
    axes[1].imshow(img_perspective)
    axes[1].set_title("Perspective Transformed Image")
    axes[1].axis('off')
    
    plt.tight_layout()
    plt.show()
