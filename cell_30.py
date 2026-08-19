import cv2
import matplotlib.pyplot as plt

# 1. Load your original image file
image_path = "your_image.jpg" 
img = cv2.imread(image_path)

if img is None:
    print(f"Error: Could not load the image '{image_path}'.")
else:
    # Convert to grayscale because thresholding relies on single-channel intensity
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 2. Apply Threshold-based Image Segmentation
    # Any pixel value above 127 becomes 255 (pure white)
    # Any pixel value below 127 becomes 0 (pure black)
    # 127 is the threshold value; 255 is the maximum value applied
    threshold_value = 127
    max_value = 255
    ret, img_segmented = cv2.threshold(img_gray, threshold_value, max_value, cv2.THRESH_BINARY)
    
    # 3. Render Image 1: The Original Grayscale Input
    plt.figure(figsize=(8, 6))
    plt.imshow(img_gray, cmap='gray')
    plt.title("Original Grayscale Image")
    plt.axis('off')
    plt.show()
    
    # 4. Render Image 2: The Segmented Binary Output
    plt.figure(figsize=(8, 6))
    plt.imshow(img_segmented, cmap='gray')
    plt.title(f"Segmented Image (Binary Threshold at {threshold_value})")
    plt.axis('off')
    plt.show()
