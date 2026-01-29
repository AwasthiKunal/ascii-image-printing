ASCII_CHARS = "@%#*+=-:. "
# pixel_value / 255 * (len(ASCII_CHARS)-1)
from PIL import Image
img = Image.open("image.png")
img = img.convert("L")
width = 100
aspect_ratio = img.height / img.width
height = int(width * aspect_ratio * 0.5)
img = img.resize((width, height))
ASCII_CHARS = "@%#*+=-:. "
pixels = img.getdata()
ascii_str = ""
for pixel in pixels:
    index = pixel * (len(ASCII_CHARS) - 1) // 255
    ascii_str += ASCII_CHARS[index]
for i in range(0, len(ascii_str), width):
    print(ascii_str[i:i+width])