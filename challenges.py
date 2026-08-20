# Challenge 1 · Create a 300×300 NumPy image and paint the Indian flag using only np.zeros and array slicing.
# Top third: [255, 153, 51] (saffron in BGR: [51, 153, 255])
# Middle third: [255, 255, 255] (white)
# Bottom third: [19, 136, 8] (green in BGR: [8, 136, 19])
# Save it as flag.png using cv2.imwrite("flag.png", img)

# Solution 1:
import numpy as np 
import matplotlib.pyplot as plt 
import cv2

# img = np.zeros((300, 300, 3), dtype=np.uint8) 
# img[0:100, :] = [51, 153, 255] # saffron (BGR) 
# img[100:200, :] = [255, 255, 255] # white 
# img[200:300, :] = [8, 136, 19] # green (BGR)
# cv2.imwrite("flag.png", img)


# Challenge 2 · Pixel inspector
# Load any image from your computer using cv2.imread(). Then:

# 1. Print its shape, dtype, and total pixel count
# 2. Print the pixel value at the exact centre of the image
# 3. Extract just the Red channel and print its average value
# 4. Convert to grayscale and save as gray_version.png

# Solution 2:
# # Load image
# img = cv2.imread("flag.png")

# # 1. Basic information
# print("Shape:", img.shape)
# print("Data type:", img.dtype)
# print("Total pixels:", img.shape[0] * img.shape[1])

# # 2. Centre pixel
# height, width = img.shape[:2]

# centre_pixel = img[height // 2, width // 2]

# print("Centre pixel (BGR):", centre_pixel)

# # 3. Red channel
# red_channel = img[:, :, 2]

# print("Average red value:", red_channel.mean())

# # 4. Convert to grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imwrite("gray_version.png", gray)


# Challenge 3 · Brightness slider (stretch goal)
# Write a function called adjust_brightness(image, value) that:

# · Takes a BGR image and an integer value (-255 to +255)
# · Returns a brightened or darkened version
# · Uses np.clip so values never go below 0 or above 255
# · Saves 3 versions: dark (-80), original, bright (+80)

# Test it on the flag you painted in Challenge 1.

# Solution 3:
def adjust_brightness(image, value):

    # Convert uint8 → float32
    adjusted = image.astype(np.float32)

    # Increase or decrease brightness
    adjusted = adjusted + value

    # Keep values between 0 and 255
    adjusted = np.clip(adjusted, 0, 255)

    # Convert back to uint8
    adjusted = adjusted.astype(np.uint8)

    return adjusted


# Test on the flag
img = cv2.imread("flag.png")

dark = adjust_brightness(img, -80)
original = adjust_brightness(img, 0)
bright = adjust_brightness(img, 80)

cv2.imwrite("flag_dark.png", dark)
cv2.imwrite("flag_original.png", original)
cv2.imwrite("flag_bright.png", bright)