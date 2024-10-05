'''
Задание 3. Создание собственных исключений. 
Напишите программу, которая вычисляет сумму списка целых чисел.
Создайте свои собственные классы исключений для обработки ситуаций, 
когда в списке есть хотя бы одно чётное или отрицательное число. 
Используйте оператор raise для генерации исключений.
'''

class MyCustomError(Exception):
    def __init__(self, message, detail):
        super().__init__(message)
        self.detail = detail

    def __str__(self):
        return f"Ошибка: {self.args[0]}. Дополнительная информация: {self.detail}"

if __name__ == '__main__':
    numbers = [1, 7, 3, 9, 5]
    sum_numbers = 0
    try:
        for number in numbers:
            if number < 0 or number % 2 == 0:
                raise MyCustomError("Список содержит отрицательные или четные числа", f"Число {number} не подходит")
            sum_numbers += number
        print(f"Сумма чисел: {sum_numbers}")  # Вывод суммы, если ошибок не было
    except MyCustomError as e:
        print(e) # Вывод сообщения об ошибке
