from PIL import Image

IMAGE_PATH = "image.png"
TARGET_WIDTH = 70      
CHAR_ASPECT = 0.45         


img = Image.open(IMAGE_PATH).convert("L")

aspect_ratio = img.height / img.width
target_height = int(TARGET_WIDTH * aspect_ratio * CHAR_ASPECT)

img = img.resize((TARGET_WIDTH, target_height))


pixels = list(img.getdata())
width, height = img.size

gray_matrix = [
    pixels[i * width:(i + 1) * width]
    for i in range(height)
]


def intensity_to_ascii(val):
    if val < 25:
        return "@"
    elif val < 50:
        return "%"
    elif val < 75:
        return "#"
    elif val < 100:
        return "*"
    elif val < 125:
        return "+"
    elif val < 150:
        return "="
    elif val < 175:
        return "-"
    elif val < 200:
        return ":"
    elif val < 225:
        return "."
    else:
        return " "

output_lines = []
for row in gray_matrix:
    line = "".join(intensity_to_ascii(val) for val in row)
    output_lines.append(line)

print("\n".join(output_lines))
