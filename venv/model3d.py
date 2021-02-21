import numpy as np
import math
from PIL import Image
# Создать класс, содержащий трёхмерную модель в виде массив трёхмерных
# координат точек (для может потребоваться создать класс трёхмерных координат).
# Считать из приложенного файла obj строки, содержащие информацию
# о вершинах модели в объект созданного класса:
# v X1 Y1 Z1
# v X2 Y2 Z2
class Model:
    points = np.empty(shape=[0, 3], dtype=np.float32)
    def __init__(self):
        points = np.empty(shape=[0,3], dtype=np.float32)
    def setPoints(self,points):
        self.points = points

    def parserOBJ(self):
        with open('Test.obj', 'r') as objFile:
            for line in objFile:
                split = line.split()
                if split[0] == "v":
                    self.points = np.append(self.points, [[float(split[1]), float(split[2]), float(split[3])]], axis=0)