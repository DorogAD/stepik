'''
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на
экран в одну строку значения, которые встречаются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
'''

a = [int(i) for i in input().split()]
b = []

for i in a:
    count = 0
    for j in a:
        if i == j:
            count += 1
            #j += 1
            if count > 1 and j not in b:
                b.append(j)

for k in b:
    print(k, end=' ')