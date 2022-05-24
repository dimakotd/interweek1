'''
Задание 1

Создать класс дробь(Fraction), конструктор которого принимает целые числа (num, den  -  числитель(numerator), знаменатель(denominator) ).

Выполнить

Атрибуты числитель и знаменатель в классе сделать приватными. Доступ к атрибутам реализовать через свойства.


Переопределить методы sub, add, mull, truediv для того, чтобы можно было выполнять соответствующие математические действия  с объектами класса дробь.

(Вычитание, сложение, умножение и деление).


Добавить класс миксин, в котором реализовать статические методы, для этих же операций(add, sub, mull, div).  

Добавить класс миксин в класс Fraction

Создать classmethod который из строки типа 'числитель/знаменатель' возвращает объект класса дробь.
Переопределить метод str, который при выводе объекта на печать будет выводить строку вида num / den.
Создать объекты класса дробь.

Выполнить все реализованные методы.
'''
import math
from random import randint

# (n * m) // math.gcd(n , m)) - наименьшее общее кратное
#  gcd(n, m) - наибольший общий делитель

class Mixin():
    @staticmethod
    def nok(n, m):
        return (n * m) // math.gcd(n , m)
    
    @staticmethod
    def sub(n, m):
        return n - m
    
    @staticmethod
    def add(n, m):
        return  n + m
    
    @staticmethod
    def mull(n, m):
        return n * m    

    @staticmethod
    def div(n, m):
        return n / m
    

class Fraction(Mixin):
    @classmethod
    def str_(cls, datastring):
        try:
            num = int(datastring.split('/')[0])
            den = int(datastring.split('/')[1])
        except:
            raise ValueError
        else:
            return Fraction(num, den)

    def __init__(self, num, den):
        self.__num = num
        self.__den = den
    
    @property
    def num(self):
        return self.__num
 
    @num.setter
    def num(self, num):
        self.__num = num

    @property
    def den(self):
        return self.__den
 
    @den.setter
    def den(self, den):
        self.__den = den


    # сумма
    def __add__(self, obj):
        den = Mixin.nok(self.den, obj.den)
        num = self.num * den // self.den + obj.num * den // obj.den
        gcd = math.gcd(den, num) 
        if gcd > 1:
            num = num // gcd
            den = den // gcd
        return Fraction(num, den)
    
    # разность
    def __sub__(self, obj):
        den = Mixin.nok(self.den, obj.den)
        num = self.num * den // self.den - obj.num * den // obj.den
        gcd = math.gcd(den, num) 
        if gcd > 1:
            num = num // gcd
            den = den // gcd
        return Fraction(num, den)
    
    # умножение
    def __mul__(self, obj):
        num =self.num * obj.num
        den =self.den * obj.den
        gcd = math.gcd(den, num) 
        if gcd > 1:
            num = num // gcd
            den = den // gcd
        return Fraction(num, den)
    
    # деление
    def __truediv__(self, obj):
        num =self.num * obj.den
        den =self.den * obj.num
        gcd = math.gcd(den, num) 
        if gcd > 1:
            num = num // gcd
            den = den // gcd
        return Fraction(num, den)
    
    def __str__(self):
        return f'{self.num} / {self.den}'
    
    
while True:
    a = Fraction.str_(input("Введите дробь в формате n/m: "))
    print(a)
    b = Fraction( randint(0, 100), randint(1, 100))
    #b = Fraction( 1, 6)
    print(b)
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    print(f"a / b = {a / b}")
    print(f"add(a, b) = {Mixin.add(a, b)}")
    print(f"sub(a, b) = {Mixin.sub(a, b)}")
    print(f"mull(a, b) = {Mixin.mull(a, b)}")
    print(f"div(a, b) = {Mixin.div(a, b)}")
