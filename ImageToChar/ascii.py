from PIL import Image
import argparse

# 字符画所使用的70个字符集
ascii_char = list(
    r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 将256灰度 映射到70个字符上
# 灰度值：指黑白图像中点的颜色深度，范围一般从0到255，白色为255，黑色为0，故黑白图片也称灰度图像


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]


def OutputAcsII(imagePath, width=80, height=80):
    im = Image.open(imagePath)
    im = im.resize((width, height), Image.NEAREST)

    txt = ''

    for i in range(height):
        for j in range(width):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'
    # print(txt)
    with open('output.txt', 'w') as f:
        f.write(txt)
