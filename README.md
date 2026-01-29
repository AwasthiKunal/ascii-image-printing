# 🎨 ASCII Art Generator - Image to ASCII Converter

> **LPU Minor Project II** | Course: Python and Full Stack  
> Converting images into ASCII art using pure Python logic and various optimization techniques

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Status](https://img.shields.io/badge/Status-Complete-green.svg)

---

## 📌 Project Overview

This project demonstrates the conversion of images into ASCII art using Python. ASCII art represents images using text characters where different characters correspond to different brightness levels. The project showcases **4 different approaches** - from pure logic-based implementation (no libraries) to enhanced versions using image processing libraries.

### 🎯 Objectives
- Understand image representation and pixel manipulation
- Apply core Python concepts: loops, conditionals, and logical operations
- Demonstrate progressive optimization techniques
- Create visually appealing ASCII art output

---

## 🖼️ Output Preview

...........................................................................
....................................:::::..................................
...................................::------:...............................
...................................::--------..............................
..................................::--========:............................
..................................::--+*****##*:...........................
...................................::-=********+=--======-:................
....................................::-==++*###############*:..............
.................................:=++*####%%%%%%%%%%%%######-..............
..........................::--=+##%%%%%#%%%%%%%%%%%%%%%####=...............
................::--==++*****####%%%%########%%%%%%%%%%%##+-...............
..........:-=+**##%%%##%%%##**+=--====+*##%%%%%%%%%%%*-....................
........-+*##%%%%%%%+==--::-=++-:..:-+#%#*+==+##%%%%%+-:...................
......:+####%%%%%%%#::...:--##*-...:+#%###***+=+*%%%*......................
......:#%%##%%%%*+*=.....:::---:...:=*##**+++=-=###+.......................
.......-*%%%%%%%=:::................-===--::::---+=*=......................
.........-=+****=:=:................:-===--::::--**+.......................
..................:.............:-..-+*==----::--=*+.......................
..............................::-:-+##+=--------==.........................
............................:-------*#%#*+=-----=:.........................
............................:::...:=+*#*+======:...........................
.................................:::--==--===+-............................
................................::::-----=++++-............................
...................................:::-=+*****=............................
......................-........:::--=++******+***+:........................
.....................-*:........::-+***#***++++*#%%+:......................
......................+-.........:-++***++++++*#%*=-:......................
.......................+-........::-======++++*#+==--:.....................
........................==:.......:::-:-=++=+*-.::---==-...................
.......................-=-::.....::::..:=++---::-==---+*-..................
.....................:+##=.::.::::-:...-++-::=+####*==+*-:.::::............
...................:-+#*-::......::-:...--::-*#*++***+=-=:...::--:.........
................:::--::..........:--...:-+##+=-::::---:::.....:--:::.......
..::::::::..::-=-:..................::-+*##+=::::::::::-----:::...:=-:.....
:::::::::::---::.::::::::.........:-=*+=--=::::::::::::::::::----=--::.....
:::::::::--:::::::::::::::::::::=+=:::-::::::::::::::::::..::--:.::........
::::::::::::::::::::::::::::::::--:::::-::::::::::::::::::....:::..........
:::::::::::::::::::::::::::::::::-::::::--::::::::::::::::....::-::........
:::::::::----:::---------::-----:---:-:=-:-:--:::::--:::::-::::--:::.......

## 📂 Project Structure

```
Img_printing/
│
├── 0.)logic.py           # Logic planning file
├── 1.) NO_LIB.py         # Pure Python - No external libraries (Manual ASCII mapping)
├── 1.) NO_LIB_Final.py   # Refined version of NO_LIB with background fill
├── 2.) SEMI_LIB.py       # Uses PIL for image loading, custom ASCII logic
├── 3.) LIB.py            # Complete PIL-based implementation
├── 4.) ENHANCED_LIB.py   # Advanced version with OpenCV edge detection
├── image.png             # Input image file
├── output.txt            # Sample ASCII output
└── README.md             # Project documentation
```

---

## 🔧 Python Concepts Used

| Concept | Application |
|---------|-------------|
| **Loops** | Iterating through pixels and rows |
| **Conditional Statements** | Mapping pixel intensity to ASCII characters |
| **Functions** | Modular code for intensity-to-ASCII conversion |
| **Lists & List Comprehension** | Storing and processing pixel data |
| **String Manipulation** | Building ASCII output strings |
| **Mathematical Operations** | Calculating aspect ratios and index mapping |

---

## 📝 Implementation Approaches

### 1️⃣ NO_LIB Approach (`1.) NO_LIB.py`)
**Pure Python - Zero External Libraries**

This approach manually defines each character position using nested loops and conditional statements. Every pixel position is hardcoded based on the image analysis.

```python
rows = 39
cols = 75

for r in range(rows):
    line = ""
    for c in range(cols):
        ch = " "
        # Row-by-row character mapping
        if r == 0:
            if c >= 34 and c <= 39:
                ch = "."
        # ... continues for all rows
```

**Key Features:**
- No dependency on external libraries
- Demonstrates pure logical thinking
- Complete control over output
- Best for understanding fundamentals

---

### 2️⃣ SEMI_LIB Approach (`2.) SEMI_LIB.py`)
**PIL for Loading + Custom Logic for Conversion**

Uses PIL library only for image loading and grayscale conversion, while the ASCII mapping logic is custom-built.

```python
from PIL import Image

def intensity_to_ascii(val):
    if val < 25:
        return "@"
    elif val < 50:
        return "%"
    elif val < 75:
        return "#"
    # ... intensity ranges for each character
```

**Key Features:**
- Custom intensity-to-ASCII function
- Manual threshold-based mapping
- Clear and readable logic
- Good balance of simplicity and functionality

---

### 3️⃣ LIB Approach (`3.) LIB.py`)
**Full PIL Implementation**

Compact implementation using PIL for all image operations with formula-based ASCII mapping.

```python
from PIL import Image

ASCII_CHARS = "@%#*+=-:. "
img = Image.open("image.png").convert("L")

# Maintain aspect ratio
width = 100
aspect_ratio = img.height / img.width
height = int(width * aspect_ratio * 0.5)
img = img.resize((width, height))

# Convert pixels to ASCII
pixels = img.getdata()
for pixel in pixels:
    index = pixel * (len(ASCII_CHARS) - 1) // 255
    ascii_str += ASCII_CHARS[index]
```

**Key Features:**
- Concise and efficient code
- Formula-based index calculation
- Automatic aspect ratio handling
- Easy to customize character set

---

### 4️⃣ ENHANCED_LIB Approach (`4.) ENHANCED_LIB.py`)
**Advanced with OpenCV Edge Detection**

The most sophisticated approach using OpenCV for histogram equalization and Canny edge detection to enhance output quality.

```python
import cv2
import numpy as np
from PIL import Image

# Enhance contrast
g = cv2.equalizeHist(g)

# Edge detection for sharper details
e = cv2.Canny(g, 80, 160)

# Combine edges with grayscale
g[e > 0] = 0
```

**Key Features:**
- Histogram equalization for better contrast
- Canny edge detection for sharper outlines
- NumPy array operations for efficiency
- Professional-quality output

---

## 🚀 How to Run

### Prerequisites
```bash
# Install required libraries
pip install Pillow
pip install opencv-python
pip install numpy
```

### Running the Scripts

```bash
# Run the pure Python version (no libraries needed)
python "1.) NO_LIB.py"

# Run the semi-library version
python "2.) SEMI_LIB.py"

# Run the full library version
python "3.) LIB.py"

# Run the enhanced version with edge detection
python "4.) ENHANCED_LIB.py"
```

### Customization

1. **Change Input Image:** Replace `image.png` with your desired image
2. **Adjust Width:** Modify the `width` or `W` variable (default: 100)
3. **Change ASCII Characters:** Modify the `ASCII_CHARS` string
   - Dense to sparse: `"@%#*+=-:. "` (dark to light)
   - More characters = more detail levels

---

## 📊 ASCII Character Mapping

The ASCII characters are arranged from **darkest** to **lightest**:

| Character | Intensity Range | Visual Density |
|:---------:|:---------------:|:--------------:|
| `@` | 0-25 | █████ Darkest |
| `%` | 26-50 | ████ |
| `#` | 51-75 | ███ |
| `*` | 76-100 | ██ |
| `+` | 101-125 | █ |
| `=` | 126-150 | ▓ |
| `-` | 151-175 | ▒ |
| `:` | 176-200 | ░ |
| `.` | 201-225 | · |
| ` ` | 226-255 | Lightest |

---

## 🧠 How It Works

### Step 1: Load Image
```
Original Image → Load into memory
```

### Step 2: Convert to Grayscale
```
RGB Image → Grayscale (0-255 per pixel)
```

### Step 3: Resize with Aspect Ratio
```
Original Size → Scaled Size (maintaining proportions)
Note: Height is multiplied by ~0.5 because characters are taller than wide
```

### Step 4: Map Pixels to ASCII
```
Pixel Value (0-255) → ASCII Character Index → Character
Formula: index = pixel_value * (num_chars - 1) // 255
```

### Step 5: Output
```
Character Array → Print row by row
```

---

## 🎓 Learning Outcomes

Through this project, I learned:

1. **Image Fundamentals** - How digital images are represented as pixel matrices
2. **Grayscale Conversion** - Converting RGB to single-channel intensity values
3. **Aspect Ratio Calculations** - Maintaining image proportions during resizing
4. **Character Mapping Logic** - Translating numerical values to visual symbols
5. **Python Proficiency** - Loops, conditionals, functions, and library usage
6. **Code Optimization** - Progressing from manual to library-based approaches

---

## 🔮 Future Enhancements

- [ ] Add color ASCII art support (ANSI colors)
- [ ] GUI interface for image selection
- [ ] Real-time webcam ASCII conversion
- [ ] HTML output with styling
- [ ] Support for video-to-ASCII conversion

---

## 👤 Author

**Student Name:** [Your Name]  
**UID:** [Your UID]  
**Course:** Python and Full Stack  
**University:** Lovely Professional University

---

## 📄 License

This project is created for educational purposes as part of LPU coursework.

---

## 🙏 Acknowledgments

- Lovely Professional University for the project opportunity
- Python and PIL/OpenCV documentation
- The open-source community for inspiration

---

<p align="center">
  <i>⭐ If you found this project helpful, please give it a star! ⭐</i>
</p>
