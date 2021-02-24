from PIL import Image
import math
import numpy as np
from model3d import Model


# алгоритмы отрисовки прямых из лекций:
# первый алгоритм:
def line1(x0, y0, x1, y1, img, color):
    t = .0
    while t < 1.0:
        x = x0 * (1. - t) + x1 * t
        y = y0 * (1. - t) + y1 * t
        img.putpixel((int(x), int(y)), color)
        t += 0.01


# второй (не работает если надо провести прямую из центра влево,
# т.к. х0>x1) y рассчитывается исходя из х :
def line2(x0, y0, x1, y1, img, color):
    x = x0
    while x <= x1:
        t = (x - x0) / (float)(x1 - x0)
        y = y0 * (1. - t) + y1 * t
        x += 1
        img.putpixel((int(x), int(y)), color)


# третий (с учетом замены если х0>x1):
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
        t = (x - x0) / (float)(x1 - x0)
        y = y0 * (1. - t) + y1 * t
        if steep:
            img.putpixel((int(x), int(y)), color)
        else:
            img.putpixel((int(y), int(x)), color)
        x += 1


# алгоритм Берзенхема:
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
    # derror – отношение сдвига по Y и сдвига
    # по X. Фактически – значение,
    # добавляемое на каждом шаге к
    # смещению по Y.
    derror = math.fabs(dy / float(dx))
    # в error накаплиивается смещение по У
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
                y -= 1
            error -= 1.
        x += 1


if __name__ == "__main__":

    h = 200
    w = 200
    # создание массива из изображения, чтобы в дальнейшем попиксельно проводить изменения
    # черное одноканальное изображение
    image = np.array(Image.new('L', (h, w)))
    # делаем белым
    for i in range(h):
        for j in range(w):
            image[i][j] = 255
    # цветное трехканальное изображение
    image = np.array(Image.new('RGB', (h, w)))
    # делаем красным
    for i in range(h):
        for j in range(w):
            image[i][j][0] = 255
    # делаем градиент
    for i in range(h):
        for j in range(w):
            image[i][j][0] = (i + j) % 256
    # достаем изображение из массива
    image = Image.fromarray(image)
    # сохраняем в файл image.png
    # для просмотра изменений нужно добавить сохранение после нужного изменения
    image.save("image.png")
    # создаем 4 черных одноканальных изображения, чтобы на них рисовать звезды
    img1 = Image.new('L', (200, 200))
    img2 = Image.new('L', (200, 200))
    img3 = Image.new('L', (200, 200))
    img4 = Image.new('L', (200, 200))
    # отрисовка 13 линий по формуле в задании 3
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
    a = Model()
    a.parserOBJ()
    h, w = 1000, 1000
    im5 = Image.new('L', (h, w))
    for i in range(15257):
        # im5.putpixel((int(50 * a.points[i][0] + 500), int(50 * int(a.points[i][1])) + 500), 255)
        # im5.putpixel((int(100 * a.points[i][0] + 500), int(100 * int(a.points[i][1])) + 500), 255)
        # im5.putpixel((int(500 * a.points[i][0] + 500), int(500 * int(a.points[i][1])) + 500), 255)
        a.points[i][0] = 4000 * a.points[i][0] + 500
        a.points[i][1] = 4000 * a.points[i][1] + 500
        im5.putpixel((int(a.points[i][0]), int(a.points[i][1])), 255)
    im5.save('image5.png')
    print(a.polyg)
    h, w = 1000, 1000
    im6 = Image.new('L', (h, w))
    print(a.points[a.polyg[i][0] - 1][0])
    for i in range(30337):
        j = 0
        while j <= 2:
            if j ==2 :
                x0 = a.points[a.polyg[i][1] - 1][0]
                y0 = a.points[a.polyg[i][1] - 1][1]
                x1 = a.points[a.polyg[i][j] - 1][0]
                y1 = a.points[a.polyg[i][j] - 1][1]
                line1(int(x0), int(y0), int(x1), int(y1), im6, 255)
                break
            x0 = a.points[a.polyg[i][0] - 1][0]
            y0 = a.points[a.polyg[i][0] - 1][1]
            x1 = a.points[a.polyg[i][j] - 1][0]
            y1 = a.points[a.polyg[i][j] - 1][1]
            j += 1
            line1(int(x0),int(y0),int(x1),int(y1),im6,255)
    im6.save('image6.png')
# im6.save('image6.png')
