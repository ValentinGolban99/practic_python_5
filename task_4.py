# Напишите программу, которая считает количество простых чисел в заданной последовательности и выводит ответ на экран.
# Простое число делится только на себя и на единицу. 
# Последовательность задаётся при помощи вызова ввода (input) на каждой итерации цикла. 
# Одна итерация — одно число.

# Пример:
# Введите количество чисел: 6.
# Введите число: 4.
# Введите число: 7.
# Введите число: 20.
# Введите число: 3.
# Введите число: 11.
# Введите число: 37.

# Количество простых чисел в последовательности: 4.

total = int(input('Введите количество чисел: ')) 
count = 0 

for number in range(1, total + 1): 
    new_number = int(input('Введите число: ')) 
    simple = True 

    for divider in range(2, number): 
        if (number % divider == 0): 
            simple = False 
        if simple: 
            count += 1  

print() 
print(f'Количество простых чисел в последовательности: {count}')
    
    