# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFilter
import random

im1 = Image.new("RGB", (512, 512))  # Создаем изображение 256 на 256 пикселей.
draw = ImageDraw.Draw(im1)  # Создаем холст для нашего фона.
width = im1.size[0]
height = im1.size[1]  # Получаем размер фона.
pix = im1.load()  # Получаем все пиксели из фона.

for x in range(width):
    for y in range(height):
        sr = random.randint(0, 255)  # Берем случайное число.
        draw.point((x, y), (sr, sr, sr))  # И рисуем его на холсте.
# По сути, ничего с фоном мы не делаем, нам просто нужен ImageDraw.Draw
# Который мы будем заполнять случайными пикселями.

im1 = im1.filter(ImageFilter.GaussianBlur(radius=3))
im1.show()


draw = ImageDraw.Draw(im1)
pix = im1.load()  # Тут загружаем данные об размытом изображении.

for x in range(width):
    for y in range(height):
        r = pix[x, y][0]  #
        g = pix[x, y][1]  # Тут как когда мы генерировали пиксельный шум, поэтому
        b = pix[x, y][2]  # не буду обьяснять.

        if r > 127:
            r = 255  #
            g = 255  # Проверяем, больше ли r 127 (это 255 / 2). Проверяем именно r
            b = 255  # Потому-что предполагается, что g и b будут ему равны, т. к. шум монохромный
        else:
            r = 0
            g = 0
            b = 0

        draw.point((x, y), (r, g, b))  # Рисуем точку на холсте.

im1.show()
