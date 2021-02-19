from PIL import Image
import matplotlib.pyplot as plt

if __name__ == "__main__":

    h = 128
    w = 128
    image = Image.new('RGB', (h, w))
    # image = Image.new('L', (h, w))
    pixels = image.load()
    for i in range(h):
        for j in range(w):
            # pixels[i, j] = 0
            # pixels[i, j] = 255
            pixels[i, j] = (i+j)%256
    image.save("image.png")
