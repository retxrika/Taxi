import os
import sys

from prettytable import *
from Lab_2 import *

# Выводит таблицу сотрудников и такси.
def print_table(taxis):
    table = PrettyTable(['№ Сотрудника', '№ Такси'])  
    data = []
    for index in range(len(taxis)):
        data.append(index + 1)
        data.append(taxis[index])

    while data:
        table.add_row(data[:2])
        data = data[2:]

    os.system('cls')
    print(table)

# Выводит сумму цифрами.
def print_sum_nums(sum):
    print(f'\nОбщая сумма, которую необходимо заплатить за просчитанный вариант (цифрами): {sum}')

# Выводит сумму словами.
def print_sum_words(sum):
    print(f'\nОбщая сумма, которую необходимо заплатить за просчитанный вариант (словами): {NumToStrWithRubs(sum)}')
    
# Возвращает корректное числовое значение из потока ввода. 
def input_num(msg):
    while True:
        try:
            num = int(input(msg + ': '))
        except:
            print('Ошибка: введено неверное значение! Попробуйте ещё раз...')
            continue
        if num < 1:
            print('Ошибка: число должно быть положительным! Попробуйте ещё раз...')
        return num

# Заполняет список чисел из потока ввода.
def fill_list_num(list_num, count, msg):
    for i in range(count):
        list_num.append(input_num(msg + ' №' + str(i + 1)))

# Выводит UI для ввода данных.
def fill_data(distances, tariffs):
    os.system('cls')
    countEmps = input_num('Введите количество сотрудников')
    fill_list_num(distances, countEmps, 'Введите количество километров до дома для сотрудника')
    fill_list_num(tariffs, countEmps, 'Введите тариф для такси')

# Возвращает сумму и список номеров такси, которые соответствуют индексу списка.
def get_sum_and_nums_taxis(distances, tariffs):
    sum = 0
    taxis = [0] * len(distances)
    for i in range(len(distances)):
        minDist = min(distances)
        maxTar = max(tariffs)
        idMinDist = distances.index(minDist)
        idMaxTar = tariffs.index(maxTar)
        
        sum += minDist * maxTar
        taxis[idMinDist] = idMaxTar + 1
        
        distances[idMinDist] = sys.maxsize
        tariffs[idMaxTar] = 0
    return sum, taxis

# Дистанции до дома и тарифы такси.
distances = []
tariffs = []

# Заполнение данных.
fill_data(distances, tariffs)

# Рассчет суммы и распределение номеров такси под индексы сотрудников.
sum, taxis = get_sum_and_nums_taxis(distances, tariffs)

# Вывод результатов.
print_table(taxis) 
print_sum_nums(sum)
print_sum_words(sum)

