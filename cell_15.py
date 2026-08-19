import cv2
import matplotlib.pyplot as plt

# 1. Load the original color image
image_path = "your_image.jpg" 
img = cv2.imread(image_path)

if img is None:
    print("Error: Could not load the image. Check the file name.")
else:
    # Convert from BGR to RGB for accurate Jupyter rendering
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    height, width, _ = img_rgb.shape
    
    # Create copies so we don't overwrite our original data matrix
    cropped_view = img_rgb.copy()
    pasted_result = img_rgb.copy()
    
    # 2. Define the coordinates for the Region of Interest (ROI)
    # We will grab a rectangular patch from the center of the image
    ymin, ymax = int(height * 0.3), int(height * 0.7)
    xmin, xmax = int(width * 0.3), int(width * 0.7)
    
    # 3. OPERATION A: Crop the ROI using NumPy slicing [rows, columns]
    roi = img_rgb[ymin:ymax, xmin:xmax]
    
    # 4. OPERATION B: Copy and Paste the ROI back onto another area of the image
    # We will paste it into the top-left corner [0, 0]
    # To prevent errors, the target space must be the exact same size as the ROI
    roi_h, roi_w, _ = roi.shape
    pasted_result[0:roi_h, 0:roi_w] = roi
    
    # 5. Display all operational stages side-by-side
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    # Original Image Panel
    axes[0].imshow(img_rgb)
    axes[0].set_title("Original Image")
    axes[0].axis('off')
    
    # Cropped ROI Panel
    axes[1].imshow(roi)
    axes[1].set_title(f"Cropped ROI ({roi_w}x{roi_h})")
    axes[1].axis('off')
    
    # Pasted Result Panel
    axes[2].imshow(pasted_result)
    axes[2].set_title("ROI Pasted to Top-Left")
    axes[2].axis('off')
    
    plt.tight_layout()
    plt.show()
