﻿'''
https://stepik.org/lesson/3367/step/3?unit=950

GC-состав является важной характеристикой геномных последовательностей и определяется 
как процентное соотношение суммы всех гуанинов и цитозинов к общему числу нуклеиновых 
оснований в геномной последовательности.

Напишите программу, которая вычисляет процентное содержание символов G (гуанин) 
и C (цитозин) в введенной строке (программа не должна зависеть от регистра вводимых символов).
'''
a = input()
s = a.lower()
l = len(s)


cnt = 0
for i in s:
    if i == 'g' or i == 'c':
        cnt = cnt + 1

res = cnt / l * 100
print(res)