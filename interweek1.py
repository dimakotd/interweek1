'''
Задание 2

Создать класс Point2D. Координаты точки задаются 2 параметрами - координатами x, y на плоскости.

Реализовать метод distance который принимает экземпляр класса Point2D и рассчитывает расстояние между 2мя точками на плоскости.

Создать защищенный атрибут класса - счетчик созданных экземпляров класса.

Чтение количества экземпляров реализовать через метод getter.



Создать класс Point3D, который является наследником класса Point2D. Координаты точки задаются 3 параметрами - координатами x, y, z в пространстве.

Переопределить конструктор с помощью super().

Переопределить метод distance для определения расстояния между 2-мя точками в пространстве.
'''

import math
from random import randint

class Point2D():
    __counter = 0

    def __new__(cls, *args, **kwargs):
        cls.__counter += 1
        return super().__new__(cls)
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'({self.x}, {self.y})'

    def getter(self):
        return Point2D.__counter

    @staticmethod
    def distance(a, b):
        if type(a) == Point2D and type(b) == Point2D:
            return math.sqrt((a.x-b.x)**2 + (a.y-b.y)**2)
        else:
            raise ValueError

class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    
    @staticmethod
    def distance(a, b):
        if type(a) == Point3D and type(b) == Point3D:
            return math.sqrt((a.x-b.x)**2 + (a.y-b.y)**2 + (a.z-b.z)**2)
        else:
            raise ValueError
    
    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'


zero2d = Point2D(0,0)
zero3d = Point3D(0,0,0)
# счетчик количества экземпляров класса стал 1 - создали нулевую точку
for i in range(5):
    a = Point2D(randint(0, 10), randint(0, 10))
    print(f'Point2D № {a.getter()} - {a} - distance = {Point2D.distance(zero2d, a)}')
    b = Point3D(randint(0, 10), randint(0, 10), randint(0, 10))
    print(f'Point3D № {b.getter()} - {b} - distance = {Point3D.distance(zero3d, b)}')

    

    