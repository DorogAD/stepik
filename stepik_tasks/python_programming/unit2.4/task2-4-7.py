﻿'''
https://stepik.org/lesson/3367/step/7?unit=950

Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики 
студенты группы информатиков предложили использовать алгоритм сжатия, 
который сжимает повторяющиеся символы в строке.

Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов 
исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и 
выводит закодированную последовательность на стандартный вывод. 
Кодирование должно учитывать регистр символов.
'''

s = input()

result = ''
new = ''
counter = 0
amount = 0
l = len(s)

for i in s:
    if new == '':
        new = i        
        amount = amount + 1
        counter = counter +1
        if l == 1:
            result = result + new + str(amount)        
    elif new == i:
        amount = amount + 1
        counter = counter +1
        if l == counter:
            result = result + new + str(amount)
    elif new != i: 
        result = result + new + str(amount)
        new = i
        amount = 1
        counter = counter + 1        
        if l == counter:
            result = result + new + str(amount)      
        

print(result)