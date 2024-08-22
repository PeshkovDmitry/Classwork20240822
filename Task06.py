"""
Задание №6
📌 Доработайте прошлую задачу добавив декоратор wraps в
каждый из декораторов.
"""

from typing import Callable
import json
import os.path
from random import randint
from functools import wraps


def check_params(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        num, cnt = args
        if num not in range(1, 101):
            new_num = randint(1, 101)
            print(f'Загаданное число изменено с {num} на {new_num}')
            num = new_num
        if cnt not in range(1, 11):
            new_cnt = randint(1, 11)
            print(f'Количество попыток изменено с {cnt} на {new_cnt}')
            cnt = new_cnt
        args = (num, cnt)
        result = func(*args, **kwargs)
        return result

    return wrapper


def save_result(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        num, cnt = args
        result = func(*args, **kwargs)
        info = []
        path = func.__name__ + '.json'
        if os.path.exists(path):
            with open(path, 'r') as f:
                info = json.load(f)
        with open(path, 'w') as f:
            info.append({'num': num, 'cnt': cnt, 'result': result})
            json.dump(info, f, indent=4)
        return result

    return wrapper


def count(num: int = 1):
    def deco(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = []
            for cnt in range(num):
                print(f'Вызов функции {func.__name__} # {cnt}')
                result.append(func(*args, **kwargs))
            return result

        return wrapper

    return deco


@check_params
@save_result
@count(2)
def attempt(num: int, cnt: int) -> bool:
    """Функция для угадывания заданного числа"""
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


print(attempt(25, 15))
print(attempt.__name__)
help(attempt)
