from PIL import Image
import math
import numpy as np

def line1(x0, y0, x1, y1, img, color):
    t = .0
    while t < 1.0:
        x = x0 * (1. - t) + x1 * t;
        y = y0 * (1. - t) + y1 * t;
        img.putpixel((int(x),int(y)), color)
        t += 0.01

def line2(x0, y0, x1, y1, img, color):
    x = x0
    while x <= x1:
        t = (x - x0)/(float)(x1 - x0);
        y = y0 * (1. - t) + y1 * t;
        x += 1
        img.putpixel((int(x), int(y)), color)

def line3(x0, y0, x1, y1, img, color):
    steep = False
    if math.fabs(x0 - x1) < math.fabs(y0 - y1):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        steep = True
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    x = x0
    while x <= x1:
        t = (x - x0)/(float)(x1 - x0);
        y = y0 * (1. - t) + y1 * t;
        if steep:
            img.putpixel((int(x), int(y)), color)
        else:
            img.putpixel((int(y), int(x)), color)
        x += 1

def lineByBresenhem(x0, y0, x1, y1, img, color):
    steep = False
    if math.fabs(x0 - x1) < math.fabs(y0 - y1):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        steep = True
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    dx = x1 - x0
    dy = y1 - y0
    derror = math.fabs(dy / float(dx))
    error = 0
    y = y0
    x = x0
    while x <= x1:
        if steep:
            img.putpixel((int(x), int(y)), color)
        else:
            img.putpixel((int(y), int(x)), color)
        error += derror
        if error > .5:
            if y1 > y0:
                y += 1
            else:
                y += -1
            error -= 1.
        x += 1

if __name__ == "__main__":

    h = 200
    w = 200
    # image = Image.new('RGB', (h, w))
    image = Image.new('L', (h, w))
    # pixels = np.asarray(image)
    pixels = image.load()
    for i in range(h):
        for j in range(w):
            pixels[i, j] = 0
            # pixels[i, j] = 255
            # pixels[i, j] = (i+j)%256
    image.save("image.png")
    img1 = Image.new('L', (200, 200))
    img2 = Image.new('L', (200, 200))
    img3 = Image.new('L', (200, 200))
    img4 = Image.new('L', (200, 200))
    for i in range(13):
        line1(100, 100, 100 + int(math.cos(i * 2 * math.pi / 13) * 95),
                  100 + int(math.sin(i * 2 * math.pi / 13) * 95), img1, 255)
        line2(100, 100, 100 + int(math.cos(i * 2 * math.pi / 13) * 95),
                  100 + int(math.sin(i * 2 * math.pi / 13) * 95), img2, 255)
        line3(100, 100, 100 + int(math.cos(i * 2 * math.pi / 13) * 95),
                  100 + int(math.sin(i * 2 * math.pi / 13) * 95), img3, 255)
        lineByBresenhem(100, 100, 100 + int(math.cos(i * 2 * math.pi / 13) * 95),
                 100 + int(math.sin(i * 2 * math.pi / 13) * 95), img4, 255)
    img1.save('image1.png')
    img2.save('image2.png')
    img3.save('image3.png')
    img4.save('imageBuiltByBresenhem.png')