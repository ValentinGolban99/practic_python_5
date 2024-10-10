# Напишите программу, которая выводит на экран равнобедренный треугольник (пирамидку), 
# заполненный символами хештега (#). Пусть высоту пирамиды определяет пользователь.

number = int(input("Введите высоту пирамиды: "))

for y in range(number):
    for x in range(-number, number * 2):

        if x >= number // 2 - y and x <= number // 2 + y:
            print('#', end='')
            
        elif x == number // 2:
            print('#', end='')

        else:
            print(' ', end='')
    print()

# Это жестко))
# Еле додумал)))
    