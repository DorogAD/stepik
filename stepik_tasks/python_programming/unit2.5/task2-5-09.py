﻿'''
https://stepik.org/lesson/3368/step/9?unit=951

Напишите программу, на вход которой подается одна строка с целыми числами.
Программа должна вывести сумму этих чисел.

Используйте метод split строки. ﻿﻿
'''

a = [int(i) for i in input().split()]

sum = 0
for i in a:
    sum = sum + i

print(sum)