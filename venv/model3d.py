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
    polyg = np.empty(shape=[0, 3], dtype=np.int)
    def __init__(self):
        polyg = np.empty(shape=[0, 3], dtype=np.int)
        points = np.empty(shape=[0,3], dtype=np.float32)
    def setPoints(self,points):
        self.points = points
    def getPoints(self):
        return self.points

    def parserOBJ(self):
        with open('Test.obj', 'r') as objFile:
            for line in objFile:
                split = line.split()
                if split[0] == "v":
                    self.points = np.append(self.points, [[float(split[1]), float(split[2]), float(split[3])]], axis=0)
                if split[0] == "f":
                    new_split1 = split[1].split('/')
                    new_split2 = split[2].split('/')
                    new_split3 = split[3].split('/')
                    self.polyg = np.append(self.polyg, [[int(new_split1[0]), int(new_split2[0]), int(new_split3[0])]], axis=0)
