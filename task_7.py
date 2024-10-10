# Напишите программу, которая получает на вход количество уровней пирамиды и выводит их на экран, заполняя нечётными числами:

height = int(input("Введите высоту пирамиды: "))
number = 1

for y in range(height):
    for x in range(-height, height * 2):

        if x >= height // 2 - y and x <= height // 2 + y:
            print(number, end='\t')
            number += 2
            
        elif x == height // 2:
            print(number, end='\t')
            number += 2

        else:
            print(' ', end='\t')
        
    print()

# По готовой 6 задаче, добавил переменную для вывода в место '#'