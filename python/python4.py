import random
import math

while(True):

    operation = input("Введите операцию (+, -, /, *, ^, abs, random, !, arccos) или exit для выхода: ")

    if (operation == "+"):

        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        print("Сумма = " + str(num1 + num2))

    elif (operation == "-"):

        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        print("Разность = " + str(num1 - num2))

    elif (operation == "/"):

        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число, отличное от нуля: "))

        while(num2 == 0):

            num2 = float(input("число не может быть нулем: "))

        print("Lеления = " + str(num1 / num2))

    elif (operation == "*"):

        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        print("Умножения = " + str(num1 * num2))

    elif (operation == "^"):

        num1 = float(input("Введите число, которое нужно возвести в степень: "))
        num2 = float(input("Введите степень числа: "))
        print("Степень числа = " + str(num1 ** num2))

    elif (operation == "abs"):

        num1 = float(input("Введите число: "))
        print("Модуль числа: " + str(abs(num1)))

    elif (operation == "random"):

        print("Рандомное число = " + str(random.randint(1, 1000)))

    elif (operation == "!"):

        num1 = int(input("Введите целое число: "))
        print("Факториал = " + str(math.factorial(num1)))

    elif (operation == "arccos"):

        num1 = float(input("Введите число от -1 до 1: "))

        while(num1 < -1 or num1 > 1):

            num1 = float(input("Введите число от -1 до 1: "))
        print("Арккосинус = " + str(math.acos(num1)))

    elif (operation == "exit"):

        break

    else :

        print("Ошибка")

print('Программа окончена')