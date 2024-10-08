"""
Задание 1. Обработка деления на ноль 
Напишите программу, которая принимает два числа от пользователя
и выводит результат их деления.
Используйте обработку исключений, чтобы корректно обработать ситуацию,
когда пользователь вводит 0 в качестве второго числа.
"""
if __name__ == "__main__":
    first_number = input("Введите первое число: ")
    second_number = input("Введите второе число: ")
    while True:  # Цикл для повторения запроса ввода при ошибке
        try:
            result = int(first_number) / int(second_number) # преобразуем строки в числа
            print("Результат деления:", result)
            break  # Выходим из цикла, если деление успешно
        except ZeroDivisionError:
            print("Делитель не может быть нулем.")
            second_number = input("Введите число, не равное нулю: ")
