import cv2
import matplotlib.pyplot as plt

# 1. Load the original color image
image_path = "your_image.jpg" 
img = cv2.imread(image_path)

if img is None:
    print("Error: Could not load the image. Check the file name.")
else:
    # Convert from BGR to RGB so colors display correctly in Jupyter
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Get original dimensions (height, width)
    height, width = img_rgb.shape[:2]
    print(f"Original Size: {width}x{height} pixels")
    
    # 2. Downscale the image to a SMALLER size (e.g., 50% of original size)
    small_width = int(width * 0.5)
    small_height = int(height * 0.5)
    img_smaller = cv2.resize(img_rgb, (small_width, small_height), interpolation=cv2.INTER_AREA)
    print(f"Smaller Size: {small_width}x{small_height} pixels")
    
    # 3. Upscale the image to a BIGGER size (e.g., 150% of original size)
    big_width = int(width * 1.5)
    big_height = int(height * 1.5)
    img_bigger = cv2.resize(img_rgb, (big_width, big_height), interpolation=cv2.INTER_CUBIC)
    print(f"Bigger Size: {big_width}x{big_height} pixels")
    
    # 4. Display all three images using subplots
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # Display Smaller Image
    axes[0].imshow(img_smaller)
    axes[0].set_title(f"Smaller ({small_width}x{small_height})")
    axes[0].axis('off')
    
    # Display Original Image
    axes[1].imshow(img_rgb)
    axes[1].set_title(f"Original ({width}x{height})")
    axes[1].axis('off')
    
    # Display Bigger Image
    axes[2].imshow(img_bigger)
    axes[2].set_title(f"Bigger ({big_width}x{big_height})")
    axes[2].axis('off')
    
    plt.tight_layout()
    plt.show()
