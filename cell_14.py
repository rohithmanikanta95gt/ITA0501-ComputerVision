import cv2
import matplotlib.pyplot as plt

# 1. Load your single image file
image_path = "your_image.jpg" 
img = cv2.imread(image_path)

if img is None:
    print("Error: Could not load the image. Check the file name.")
else:
    # Convert from BGR to RGB for Jupyter display
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Create a clean copy to apply the text watermark onto
    watermarked_image = img_rgb.copy()
    
    # 2. Configure text settings
    watermark_text = "© CONFIDENTIAL - CV LAB" # Change this text to your choice
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    # Calculate text scaling dynamically based on image width
    height, width, _ = watermarked_image.shape
    font_scale = width / 1000.0  # Scales nicely for both small and large images
    thickness = max(2, int(font_scale * 2))
    
    # 3. Get exact pixel dimensions of the text block to position it safely
    (text_w, text_h), baseline = cv2.getTextSize(watermark_text, font, font_scale, thickness)
    
    # Calculate bottom-right corner positioning coordinates with padding
    margin = 30
    x_pos = width - text_w - margin
    y_pos = height - margin
    
    # 4. Burn the text watermark directly onto the image
    # Parameters: image, text, (x, y) coordinates, font, scale, color (R, G, B), thickness, lineType
    cv2.putText(watermarked_image, watermark_text, (x_pos, y_pos), font, font_scale, (255, 255, 255), thickness, cv2.LINE_AA)
    
    # 5. Display the comparison side-by-side
    fig, axes = plt.subplots(1, 2, figsize=(16, 8))
    
    axes[0].imshow(img_rgb)
    axes[0].set_title("Original Image")
    axes[0].axis('off')
    
    axes[1].imshow(watermarked_image)
    axes[1].set_title("Text Watermarked Image")
    axes[1].axis('off')
    
    plt.tight_layout()
    plt.show()
