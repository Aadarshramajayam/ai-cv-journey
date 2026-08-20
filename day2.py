import numpy as np 
import cv2 
import matplotlib.pyplot as plt 

# ── 1. Create a fake image from scratch
img = np.zeros((300, 300, 3), dtype=np.uint8) 

# Paint a red square in the middle 
img[100:200, 100:200] = [0, 0, 255] 

# BGR in OpenCV! # ── 2. Inspect it
print("Shape:", img.shape) print("Dtype:", img.dtype) print("Pixel at (150,150):", img[150, 150]) 

# ── 3. Brighten it
img_float = img.astype(np.float32) 
bright = np.clip(img_float + 80, 0, 255).astype(np.uint8) 

# ── 4. Convert to grayscale 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

# ── 5. Show all three versions 
fig, axes = plt.subplots(1, 3, figsize=(12, 4)) axes[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) axes[0].set_title("Original") 
axes[1].imshow(cv2.cvtColor(bright, cv2.COLOR_BGR2RGB)) 
axes[1].set_title("Brightened") 
axes[2].imshow(gray, cmap="gray") 
axes[2].set_title("Grayscale") 
plt.tight_layout() 
plt.savefig("day2_output.png") 
plt.show() 
print("Saved to day2_output.png")



