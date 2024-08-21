"""
Задание №1
📌 Создайте функцию-замыкание, которая запрашивает два целых числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
📌 Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.
"""

from typing import Callable


def set_num(num: int) -> Callable:
    def set_attempt_count(cnt: int) -> bool:
        current_attempt: int = 0
        while current_attempt < cnt:
            num_from_console = int(input("Введите число -> "))
            if num_from_console == num:
                return True
            current_attempt += 1
        return False

    return set_attempt_count


run = set_num(25)
if run(5):
    print("Вы угадали")
else:
    print("Попытки закончились")
