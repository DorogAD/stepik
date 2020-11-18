﻿'''
https://stepik.org/lesson/3373/step/7?unit=956

Напишите программу, которая считывает строку с числом n, которое задаёт количество чисел,
которые нужно считать. Далее считывает n строк с числами X i-тое​, по одному числу в каждой строке.
Итого будет n+1 строк.

При считывании числа X i-тое​ программа должна на отдельной строке вывести значение f(Xi).
Функция f(x) уже реализована и доступна для вызова.

Функция вычисляется достаточно долго и зависит только от переданного аргумента x.
Для того, чтобы уложиться в ограничение по времени, нужно избежать повторного вычисления значений.

тестовая функция

def f(number):
    return (number * 3 + 1)
'''

a = int(input())
s = []
for i in range(a):
    num = int(input())
    s.append(num)

d = {}
for i in s:
    if i in d:
        print(d[i])
    else:
        res = f(i)
        print(res)
        d[i] = res