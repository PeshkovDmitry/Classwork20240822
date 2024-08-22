"""
Задание №4
📌 Создайте декоратор с параметром.
📌 Параметр - целое число, количество запусков декорируемой
функции.
"""

from typing import Callable


def count(num: int = 1):
    def deco(func: Callable):
        def wrapper(*args, **kwargs):
            result = []
            for cnt in range(num):
                print(f'Вызов функции {func.__name__} # {cnt}')
                result.append(func(*args, **kwargs))
            return result

        return wrapper

    return deco


@count(5)
def attempt(num: int, cnt: int) -> bool:
    current_attempt: int = 0
    while current_attempt < cnt:
        num_from_console = int(input("Введите число -> "))
        if num_from_console == num:
            print("Вы угадали")
            return True
        current_attempt += 1
        print("Вы не угадали")
    print("Попытки закончились")
    return False


print(attempt(25, 5))
