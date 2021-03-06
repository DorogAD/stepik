﻿'''
https://stepik.org/lesson/3368/step/10?unit=951

Напишите программу, на вход которой подаётся список чисел одной строкой.
Программа должна для каждого элемента этого списка вывести сумму двух его соседей.
Для элементов списка, являющихся крайними, одним из соседей считается элемент,
находящий на противоположном конце этого списка.
Например, если на вход подаётся список "1 3 5 6 10",
то на выход ожидается список "13 6 9 15 7" (без кавычек).

Если на вход пришло только одно число, надо вывести его же.

Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
'''

a = [int(i) for i in input().split()]
length = len(a)

if length == 1:
    print(a[0])
elif length == 2:
    print((a[1] + a[1]), a[0] + a[0])
else:
    sum = 0
    num1 = 0
    num2 = 0
    for i in range(length):
        if i == length - 1:
            num1 = a[i - 1]
            num2 = a[0]
            sum = num1 + num2
            print(sum, end=' ')
        else:
            num1 = a[i - 1]
            num2 = a[i + 1]
            sum = num1 + num2
            print(sum, end=' ')
