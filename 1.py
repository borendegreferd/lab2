'''Написать программу для поиска действительных корней квадратного уравнения.'''
import math
a=int(input())
b=int(input())
c=int(input())
d=b*b-4*a*c
if d>0:
    print('Первый корень {0}\nВторой корень {1}'.format((-b - math.sqrt(d)) / (2 * a),(-b + math.sqrt(d)) / (2 * a)))
else: print('Нет действительных корней')