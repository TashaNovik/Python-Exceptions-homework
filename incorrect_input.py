"""
Задание 2. Обработка некорректного ввода 
Расширьте предыдущую программу, 
чтобы она также обрабатывала ситуацию, 
когда пользователь вводит строку вместо числа. 
Используйте несколько блоков except для обработки разных типов исключений.
"""

if __name__ == "__main__":
    while True:
        try:
            first_number_str = input("Введите первое число: ")
            first_number = int(first_number_str)

            while True: # Вложенный цикл для второго числа
                try:
                    second_number_str = input("Введите второе число: ")
                    second_number = int(second_number_str)
                    if second_number == 0:
                        raise ZeroDivisionError("Делитель не может быть нулем.")
                    break  # Выход из внутреннего цикла, если второе число корректно
                except ValueError:
                    print("Некорректный ввод второго числа. Повторите ввод.")
                except ZeroDivisionError as e:
                    print(e)

            result = first_number / second_number
            print("Результат деления:", result)
            break  # Выход из внешнего цикла, если оба числа корректны

        except ValueError:
            print("Некорректный ввод первого числа. Повторите ввод.")



