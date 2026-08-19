import cv2

# Step 1: Read the original image
img_color = cv2.imread("your_image.jpg") 

if img_color is None:
    print("Error: Could not load the image.")
else:
    # Step 2: Apply Gaussian Blur
    # (15, 15) is the kernel size (must be odd numbers). Higher numbers = more blur.
    # 0 tells OpenCV to automatically calculate the standard deviation based on kernel size.
    img_blur = cv2.GaussianBlur(img_color, (15, 15), 0)
    
    # Step 3: Create resizable windows so they aren't zoomed in
    cv2.namedWindow("Original Color", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Gaussian Blur Result", cv2.WINDOW_NORMAL)
    
    # Set display sizes for your monitor
    cv2.resizeWindow("Original Color", 600, 450)
    cv2.resizeWindow("Gaussian Blur Result", 600, 450)
    
    # Step 4: Display both the original and blurred images
    cv2.imshow("Original Color", img_color)
    cv2.imshow("Gaussian Blur Result", img_blur)
    
    # Keep windows open until a key is pressed
    cv2.waitKey(0) 
    cv2.destroyAllWindows()

