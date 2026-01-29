import cv2
import numpy as np
from PIL import Image

ASCII = "@%#*+=-:. "
IMG = "image.png"
W = 100
CHAR_AR = 0.45

# load grayscale
img = Image.open(IMG).convert("L")

# resize without distortion
w, h = img.size
nh = int(W * h / w * CHAR_AR)
img = img.resize((W, nh))

# to numpy
g = np.array(img)

# enhance contrast
g = cv2.equalizeHist(g)

# edge detection
e = cv2.Canny(g, 80, 160)

# combine edges
g[e > 0] = 0

# ascii render
out = []
for row in g:
    line = ""
    for px in row:
        idx = int(px) * (len(ASCII) - 1) // 255 
        line += ASCII[idx]
    out.append(line)

print("\n".join(out))
