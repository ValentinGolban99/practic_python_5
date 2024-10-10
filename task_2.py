# Напишите программу, которая выводит «лестницу» из чисел, когда пользователь вводит число N:

n = int(input("Введите размер матрицы: "))

for y in range(1, n + 1):
    for x in range(1, n + 1):
        
        if y > x:
            print(y, end='\t')
        elif y == x:
            print(y, end='\t')
        else:
            print('', end='\t')
    print()