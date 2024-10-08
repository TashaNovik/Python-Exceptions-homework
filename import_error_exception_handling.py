'''
Задание 6. Обработка ошибок импорта модулей.
 Напишите программу, которая импортирует модуль math
 и использует функцию sqrt() для вычисления квадратного корня числа,
 введённого пользователем. Используйте обработку исключений для корректной обработки ситуаций,
 когда модуль math не может быть импортирован или функция sqrt() не может быть вызвана для отрицательного числа.
'''


if __name__ == '__main__':
    try:
        import math
    except ImportError:
        print("Модуль math не найден!")
    else:
        try:
            number_str = input("Введите число: ")
            number = float(number_str)  # Преобразование строки в число
            if number < 0:
                raise ValueError("Квадратный корень из отрицательного числа вычислить нельзя")
            result = math.sqrt(number)
            print(f"Квадратный корень из {number} равен {result}")
        except ValueError as e:
            print(f"Ошибка преобразования: {e}")  # Более информативное сообщение об ошибке
        except Exception as e:
            print(f"Произошла неизвестная ошибка: {e}")