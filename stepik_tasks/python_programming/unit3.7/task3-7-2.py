"""
https://stepik.org/lesson/3380/step/2?unit=963

В какой-то момент в Институте биоинформатики биологи перестали понимать, что говорят информатики: они говорили каким-то
странным набором звуков.

В какой-то момент один из биологов раскрыл секрет информатиков: они использовали при общении подстановочный шифр, т.е.
заменяли каждый символ исходного сообщения на соответствующий ему другой символ.
Биологи раздобыли ключ к шифру и теперь нуждаются в помощи:

Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две строки
одинаковой длины, на первой строке записаны символы исходного алфавита, на второй строке — символы конечного алфавита,
после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.

Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки,
которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac
"""

# key_example = [i for i in input()]
# key_code = [i for i in input()]
# key_dict = dict(zip(key_example, key_code))
# encode = input()
# decode = input()

key_dict = {'a': '*', 'b': 'd', 'c': '%', 'd': '#'}
encode = 'abacabadaba'
decode = '#*%*d*%'

encode_result = ''
for i in encode:
    for j in key_dict:
        if i == j:
            encode_result += key_dict[j]

decode_result = ''
for i in decode:
    for j in key_dict:
        if i == key_dict[j]:
            decode_result += j

print(encode_result)
print(decode_result)
