import cv2

# Step 1: Read the original image
img_color = cv2.imread("your_image.jpg") 

if img_color is None:
    print("Error: Could not load the image.")
else:
    # Step 2: Apply Canny Edge Detection
    # 100 is the first threshold (lower limit)
    # 200 is the second threshold (upper limit)
    img_edges = cv2.Canny(img_color, 100, 200)
    
    # Step 3: Create resizable windows so they aren't zoomed in
    cv2.namedWindow("Original Color", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Canny Outlines", cv2.WINDOW_NORMAL)
    
    # Set display sizes for your monitor
    cv2.resizeWindow("Original Color", 600, 450)
    cv2.resizeWindow("Canny Outlines", 600, 450)
    
    # Step 4: Display both the original and outline images
    cv2.imshow("Original Color", img_color)
    cv2.imshow("Canny Outlines", img_edges)
    
    # Keep windows open until a key is pressed
    cv2.waitKey(0) 
    cv2.destroyAllWindows()
