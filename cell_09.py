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
    
    # 2. Perform 90-degree clockwise rotation
    img_90 = cv2.rotate(img_rgb, cv2.ROTATE_90_CLOCKWISE)
    
    # 3. Perform 180-degree clockwise rotation
    img_180 = cv2.rotate(img_rgb, cv2.ROTATE_180)
    
    # 4. Perform 270-degree clockwise rotation (equivalent to 90 counter-clockwise)
    img_270 = cv2.rotate(img_rgb, cv2.ROTATE_90_COUNTERCLOCKWISE)
    
    # 5. Create a 1x4 subplot grid to compare all results side-by-side
    fig, axes = plt.subplots(1, 4, figsize=(20, 5))
    
    # Display Original Image
    axes[0].imshow(img_rgb)
    axes[0].set_title("Original Image")
    axes[0].axis('off')
    
    # Display 90 Degree Rotation
    axes[1].imshow(img_90)
    axes[1].set_title("90° Clockwise")
    axes[1].axis('off')
    
    # Display 180 Degree Rotation
    axes[2].imshow(img_180)
    axes[2].set_title("180° Clockwise")
    axes[2].axis('off')
    
    # Display 270 Degree Rotation
    axes[3].imshow(img_270)
    axes[3].set_title("270° Clockwise")
    axes[3].axis('off')
    
    # Adjust layout and display the final plots
    plt.tight_layout()
    plt.show()
