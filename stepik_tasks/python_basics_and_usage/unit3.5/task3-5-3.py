"""
https://stepik.org/lesson/24476/step/3?unit=6781


В этой задаче вам необходимо воспользоваться API сайта http://numbersapi.com/

Вам дается набор чисел. Для каждого из чисел необходимо узнать,
существует ли интересный математический факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.

Пример запроса к интересному числу:
http://numbersapi.com/31/math?json=true

Пример запроса к скучному числу:
http://numbersapi.com/999/math?json=true

Пример входного файла:
31
999
1024
502

Пример выходного файла:
Interesting
Boring
Interesting
Boring
"""
import requests

lst = []
with open('dataset_24476_3.txt', 'r') as f:
    for line in f:
        lst.append(line.strip())

for number in lst:
    api_url = 'http://numbersapi.com/' + str(number) + '/math?json=true'
    params = {
        'json': number,
    }
    res = requests.get(api_url, params=params)
    data = res.json()
    if data['found']:
        print('Interesting')
    else:
        print('Boring')
