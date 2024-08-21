"""
Задание №2
📌 Дорабатываем задачу 1.
📌 Превратите внешнюю функцию в декоратор.
📌 Он должен проверять входят ли переданные в функцию-
угадайку числа в диапазоны [1, 100] и [1, 10].
📌 Если не входят, вызывать функцию со случайными числами
из диапазонов.
"""

from typing import Callable
from random import randint


def main(func: Callable):
    def wrapper(*args, **kwargs):
        print(f'Запуск функции {func.__name__}')
        num = args[0]
        attempt_cnt = args[1]
        if num not in range(1, 101):
            new_num = randint(1, 101)
            print(f'Загаданное число изменено с {num} на {new_num}')
            num = new_num
        if attempt_cnt not in range(1, 11):
            new_attempt_cnt = randint(1, 11)
            print(f'Количество попыток изменено с {attempt_cnt} на {new_attempt_cnt}')
            attempt_cnt = new_attempt_cnt
        args = (num, attempt_cnt)
        result = func(*args, **kwargs)
        print(f'Завершение функции {func.__name__}')
        return result
    return wrapper


def attemp(num: int, cnt: int) -> bool:
    current_attempt: int = 0
    while current_attempt < cnt:
        num_from_console = int(input("Введите число -> "))
        if num_from_console == num:
            return True
        current_attempt += 1
    return False


run = main(attemp)
if run(25, 15):
    print("Вы угадали")
else:
    print("Попытки закончились")
