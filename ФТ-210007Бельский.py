import os
import sys

from prettytable import *
from Lab_2 import *

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

def print_sum(sum):
    print(f'\nОбщая сумма, которую необходимо заплатить за просчитанный вариант: {NumToStrWithRubs(sum)}')
    
def input_num(msg):
    while True:
        try:
            num = int(input(msg + ': '))
        except:
            print('Ошибка: введено неверное значение! Попробуйте ещё раз...')
            continue
        return num

def fill_list_num(list_num, count, msg):
    for i in range(count):
        list_num.append(input_num(msg + ' №' + str(i + 1)))

def fill_data(distances, tariffs):
    os.system('cls')
    countEmps = input_num('Введите количество сотрудников')
    fill_list_num(distances, countEmps, 'Введите количество километров до дома для сотрудника')
    fill_list_num(tariffs, countEmps, 'Введите тариф для такси')

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

distances = []
tariffs = []

fill_data(distances, tariffs)

sum, taxis = get_sum_and_nums_taxis(distances, tariffs)

print_table(taxis)
print_sum(sum)

